from flask import Flask
import os
import opengradient as og

app = Flask(__name__)

def get_models():

    try:

        hub = og.ModelHub(
            email=os.getenv("OG_EMAIL"),
            password=os.getenv("OG_PASSWORD")
        )

        models = hub.list_models()

        results = []

        for m in models[:10]:

            results.append({
                "name": m["name"],
                "description": m.get("description","OpenGradient model")
            })

        return results

    except:

        return [
            {"name":"ETH Volatility Predictor","description":"Predict ETH volatility"},
            {"name":"Crypto Sentiment AI","description":"Analyze crypto sentiment"}
        ]


@app.route("/")
def home():

    models = get_models()

    cards = ""

    for m in models:

        cards += f"""
        <div class='card'>
        <h3>{m["name"]}</h3>
        <p>{m["description"]}</p>
        </div>
        """

    return f"""
<!DOCTYPE html>

<html>

<head>

<title>OpenGradient Models</title>

<style>

body{{
background:#0b0f1a;
color:white;
font-family:Arial;
margin:0;
}}

.header{{
text-align:center;
padding:40px;
}}

.title{{
font-size:36px;
color:#00f2ff;
}}

.grid{{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
padding:40px;
}}

.card{{
background:#141a2b;
padding:20px;
border-radius:10px;
}}

.card:hover{{
background:#1c2338;
}}

</style>

</head>

<body>

<div class="header">

<div class="title">

OpenGradient Model Explorer

</div>

</div>

<div class="grid">

{cards}

</div>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
