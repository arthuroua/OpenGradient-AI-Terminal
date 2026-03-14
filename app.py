from flask import Flask
import requests

app = Flask(__name__)

API = "https://hub.opengradient.ai/api/models?page=0&limit=50&sort_by=most_likes"

def fetch_models():

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:

        r = requests.get(API, headers=headers, timeout=10)

        data = r.json()

        return data.get("models", [])

    except:

        return []


def ecosystem_stats(models):

    total = len(models)

    total_likes = sum(m.get("likes",0) for m in models)

    top_model = ""

    if models:
        top_model = models[0].get("name","")

    return total, total_likes, top_model


@app.route("/")
def home():

    models = fetch_models()

    total, likes, top = ecosystem_stats(models)

    cards = ""

    for m in models[:20]:

        cards += f"""

        <div class='card'>

        <h3>{m.get('name')}</h3>

        <p>{m.get('description','OpenGradient model')}</p>

        <div class='likes'>❤️ {m.get('likes',0)}</div>

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
font-size:40px;
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
min-width:150px;
text-align:center;
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

<div class="stats">

<div class="stat">
Models<br>
<b>{total}</b>
</div>

<div class="stat">
Total Likes<br>
<b>{likes}</b>
</div>

<div class="stat">
Top Model<br>
<b>{top}</b>
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
