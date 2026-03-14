from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = "https://hub.opengradient.ai/models"


def get_models():

    models = []

    try:

        headers = {
        "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(URL, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup.find_all("h3"):

            name = tag.text.strip()

            if len(name) > 3 and len(name) < 80:

                models.append({
                    "name": name,
                    "description": "OpenGradient model"
                })

        models = list(dict.fromkeys([m["name"] for m in models]))

        result = []

        for m in models[:20]:

            result.append({
                "name": m,
                "description": "Model from OpenGradient Hub"
            })

        if len(result) > 0:
            return result

    except Exception as e:

        print("scraper error:", e)

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

    total_models = len(models)

    return f"""
<!DOCTYPE html>

<html>

<head>

<title>OpenGradient Ecosystem Radar</title>

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

.stats{{
display:flex;
justify-content:center;
padding:20px;
}}

.stat{{
background:#141a2b;
padding:20px;
border-radius:10px;
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

OpenGradient Ecosystem Radar

</div>

</div>

<div class="stats">

<div class="stat">

Detected Models<br>
<b>{total_models}</b>

</div>

</div>

<div class="grid">

{cards}

</div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
