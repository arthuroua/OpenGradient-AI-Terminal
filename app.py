from flask import Flask
import requests

app = Flask(__name__)

API = "https://hub.opengradient.ai/api/models?page=0&limit=20&sort_by=most_likes"

def get_models():

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:

        r = requests.get(API, headers=headers, timeout=10)

        data = r.json()

        models = []

        for m in data.get("models", []):

            models.append({
                "name": m.get("name","Unknown Model"),
                "description": m.get("description","OpenGradient model"),
                "likes": m.get("likes",0)
            })

        return models

    except Exception as e:

        print("API error:", e)

        return []

@app.route("/")
def home():

    models = get_models()

    cards = ""

    for m in models:

        cards += f"""
        <div class='card'>
        <h3>{m['name']}</h3>
        <p>{m['description']}</p>
        <div class='likes'>❤️ {m['likes']}</div>
        </div>
        """

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

.grid{{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
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
margin-top:10px;
color:#00f2ff;
}}

</style>

</head>

<body>

<div class="header">
<div class="title">
OpenGradient Ecosystem Radar
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
