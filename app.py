from flask import Flask
import requests

app = Flask(__name__)

API_URL = "https://hub.opengradient.ai/models?page=0&limit=24&search=&sort_by=most_likes"

def get_models():

    try:

        headers = {
        "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(API_URL, headers=headers, timeout=10)

        data = r.json()

        models = []

        for m in data.get("models", []):

            models.append({
                "name": m.get("name","Unknown Model"),
                "description": m.get("description","OpenGradient model"),
                "likes": m.get("likes",0)
            })

        if len(models) > 0:
            return models

    except Exception as e:
        print("API error:", e)

    return [
        {"name":"ETH Volatility Predictor","description":"Predict ETH volatility","likes":0},
        {"name":"Crypto Sentiment AI","description":"Analyze crypto sentiment","likes":0}
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
        <p class='likes'>❤️ {m["likes"]}</p>
        </div>
        """

    total_models = len(models)
    total_likes = sum(m["likes"] for m in models)

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
gap:40px;
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

.likes{{
color:#00f2ff;
font-weight:bold;
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
Total Models<br>
<b>{total_models}</b>
</div>

<div class="stat">
Total Likes<br>
<b>{total_likes}</b>
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
