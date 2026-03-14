from flask import Flask
import requests
import random

app = Flask(__name__)

API_URL = "https://hub.opengradient.ai/api/models?page=0&limit=24&sort_by=most_likes"

signals = [
"BULLISH",
"BEARISH",
"HIGH VOLATILITY",
"POSITIVE SENTIMENT"
]

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
        {"name":"ETH Volatility Predictor","description":"Predict ETH volatility"},
        {"name":"Crypto Sentiment AI","description":"Analyze crypto sentiment"}
    ]

@app.route("/")
def home():

    models = get_models()

    cards = ""

    for m in models:

        confidence = random.randint(60,95)
        signal = random.choice(signals)

        size = confidence * 2

        if confidence > 85:
            color = "#16c784"
        elif confidence > 70:
            color = "#f3ba2f"
        else:
            color = "#ea3943"

        name = m["name"].replace("'","")

        cards += f"""
        <div class='tile'
        onclick="showModel('{name}','{signal}','{confidence}','{m["description"]}','{m["likes"]}')"
        style='width:{size}px;height:{size}px;background:{color};'>

        <div class='tile-title'>{name}</div>
        <div>{signal}</div>
        <div class='tile-score'>{confidence}%</div>

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
background:#05070d;
color:white;
font-family:Arial;
margin:0;
}}

.header{{
text-align:center;
padding:40px;
}}

.title{{
font-size:42px;
color:#00f2ff;
}}

.stats{{
display:flex;
justify-content:center;
gap:40px;
padding:20px;
}}

.stat{{
background:#0f1424;
padding:20px;
border-radius:10px;
text-align:center;
}}

.heatmap{{
display:flex;
flex-wrap:wrap;
gap:12px;
justify-content:center;
padding:20px;
}}

.tile{{
border-radius:10px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
font-size:12px;
padding:10px;
cursor:pointer;
transition:0.2s;
}}

.tile:hover{{
transform:scale(1.1);
}}

.panel{{
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
background:#0f1424;
padding:25px;
border-radius:10px;
width:320px;
display:none;
}}

.activity{{
max-width:800px;
margin:30px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
}}

.event{{
border-bottom:1px solid #1c233a;
padding:6px 0;
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

<div class="heatmap">
{cards}
</div>

<div class="activity">

<h3>⚡ Live Model Activity</h3>

<div id="feed"></div>

</div>

<div id="panel" class="panel"></div>

<script>

const signals=[
"HIGH VOLATILITY",
"BULLISH TREND",
"BEARISH SIGNAL",
"POSITIVE SENTIMENT"
]

function addEvent(){{

let time=new Date().toLocaleTimeString()

let s=signals[Math.floor(Math.random()*signals.length)]

let text="["+time+"] model signal → "+s

let feed=document.getElementById("feed")

let div=document.createElement("div")

div.className="event"

div.innerText=text

feed.prepend(div)

if(feed.children.length>10){{
feed.removeChild(feed.lastChild)
}}

}}

setInterval(addEvent,3000)

function showModel(name,signal,confidence,desc,likes){{

let panel=document.getElementById("panel")

panel.style.display="block"

panel.innerHTML="<h2>"+name+"</h2>"
+"<p><b>Signal:</b> "+signal+"</p>"
+"<p><b>Confidence:</b> "+confidence+"%</p>"
+"<p><b>Likes:</b> "+likes+"</p>"
+"<p>"+desc+"</p>"
+"<button onclick='closePanel()'>Close</button>"

}}

function closePanel(){{
document.getElementById("panel").style.display="none"
}}

</script>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
