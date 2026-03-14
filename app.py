from flask import Flask
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

signals = [
"Bullish",
"Bearish",
"High Volatility",
"Positive Sentiment",
"Risk Increase"
]

def get_models():

    try:

        url="https://hub.opengradient.ai"

        r=requests.get(url,timeout=5)

        soup=BeautifulSoup(r.text,"html.parser")

        models=[]

        for h in soup.find_all("h3")[:12]:

            name=h.text.strip()

            if len(name)>2:

                models.append({
                    "name":name,
                    "description":"OpenGradient Model"
                })

        if len(models)>0:
            return models

    except Exception as e:

        print("Hub error:",e)

    return [
        {"name":"ETH Volatility Predictor","description":"Predict ETH volatility"},
        {"name":"Crypto Sentiment AI","description":"Analyze sentiment"}
    ]


@app.route("/")
def home():

    models=get_models()

    cards=""

    for m in models:

        confidence=random.randint(60,95)
        signal=random.choice(signals)

        size=confidence*2

        if confidence>85:
            color="#16c784"
        elif confidence>70:
            color="#f3ba2f"
        else:
            color="#ea3943"

        name=m["name"].replace("'","")

        cards+=f"""
        <div class='tile'
        onclick="showModel('{name}','{signal}','{confidence}','{m["description"]}')"
        style='width:{size}px;height:{size}px;background:{color};'>

        <div class='tile-title'>{name}</div>
        <div>{signal}</div>
        <div class='tile-score'>{confidence}%</div>

        </div>
        """

    return f"""
<!DOCTYPE html>

<html>

<head>

<title>OpenGradient Model Radar</title>

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
font-size:44px;
color:#00f2ff;
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

.watchlist{{
max-width:800px;
margin:30px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
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

OpenGradient Model Radar

</div>

</div>

<div class="heatmap">

{cards}

</div>

<div class="watchlist">

<h3>⭐ Watchlist</h3>

<div id="watchlist"></div>

</div>

<div class="activity">

<h3>⚡ Live Model Activity</h3>

<div id="feed"></div>

</div>

<div class="activity">

<h3>🆕 New Models Monitor</h3>

<div id="monitor"></div>

</div>

<div id="panel" class="panel"></div>

<script>

let watchlist=[]

function addWatch(name){{

if(!watchlist.includes(name)){{

watchlist.push(name)

renderWatch()

}}

}}

function renderWatch(){{

let box=document.getElementById("watchlist")

box.innerHTML=""

watchlist.forEach(m=>{{
box.innerHTML+="<div class='event'>⭐ "+m+"</div>"
}})

}}

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

}}

setInterval(addEvent,3000)

function monitorModel(){{

let time=new Date().toLocaleTimeString()

let text="["+time+"] new model detected"

let box=document.getElementById("monitor")

let div=document.createElement("div")

div.className="event"

div.innerText=text

box.prepend(div)

}}

setInterval(monitorModel,7000)

function showModel(name,signal,confidence,desc){{

addWatch(name)

let panel=document.getElementById("panel")

panel.style.display="block"

panel.innerHTML="<h2>"+name+"</h2>"
+"<p><b>Signal:</b> "+signal+"</p>"
+"<p><b>Confidence:</b> "+confidence+"%</p>"
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
    app.run(host="0.0.0.0",port=8080)
