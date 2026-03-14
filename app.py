from flask import Flask
import random
import requests

app = Flask(__name__)

fallback_models = [
("ETH Volatility Predictor","Predict ETH volatility"),
("Crypto Sentiment AI","Analyze market sentiment"),
("Market Regime Detector","Detect bull/bear regimes"),
("BTC Price Predictor","Forecast BTC trends"),
("DeFi Risk Analyzer","Analyze DeFi risk")
]

signals = [
"Bullish",
"Bearish",
"High Volatility",
"Positive Sentiment",
"Risk Increase"
]


def get_models():

    try:
        r = requests.get("https://hub.opengradient.ai",timeout=5)

        if r.status_code == 200:

            text = r.text

            models=[]

            lines=text.split(">")

            for l in lines:

                if "Model" in l or "Predictor" in l:

                    name=l.strip()

                    if len(name)<40:

                        models.append((name,"OpenGradient model"))

                if len(models)>6:
                    break

            if len(models)>2:
                return models

    except:
        pass

    return fallback_models


@app.route("/")
def home():

    models=get_models()

    cards=""

    for name,desc in models:

        confidence=random.randint(60,95)
        signal=random.choice(signals)

        size=confidence*2

        if confidence>80:
            color="#16c784"
        elif confidence>70:
            color="#f3ba2f"
        else:
            color="#ea3943"

        safe=name.replace("'","")

        cards+=f"""
        <div class="tile" onclick="showModel('{safe}','{signal}','{confidence}','{desc}')" style="width:{size}px;height:{size}px;background:{color};">
        <div class="tile-title">{name}</div>
        <div>{signal}</div>
        <div class="tile-score">{confidence}%</div>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>

<head>

<title>OpenGradient AI Terminal</title>

<style>

body {{
background:#05070d;
color:white;
font-family:Arial;
margin:0;
}}

.header {{
text-align:center;
padding:40px;
}}

.title {{
font-size:42px;
font-weight:bold;
background:linear-gradient(90deg,#00f2ff,#8a5cff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}}

.heatmap {{
display:flex;
flex-wrap:wrap;
gap:10px;
justify-content:center;
padding:20px;
}}

.tile {{
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

.tile:hover {{
transform:scale(1.1);
}}

.tile-title {{
font-weight:bold;
margin-bottom:4px;
}}

.tile-score {{
font-size:16px;
font-weight:bold;
margin-top:4px;
}}

.panel {{
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

.timeline {{
margin-top:10px;
font-size:13px;
}}

.close {{
margin-top:10px;
cursor:pointer;
color:#00f2ff;
}}

.activity {{
max-width:700px;
margin:40px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
}}

.event {{
border-bottom:1px solid #1c233a;
padding:5px 0;
}}

</style>

</head>

<body>

<div class="header">

<div class="title">OpenGradient AI Terminal</div>

</div>

<div class="heatmap">

{cards}

</div>


<div class="activity">

<h3>⚡ Live Model Activity</h3>

<div id="feed"></div>

</div>


<div class="activity">

<h3>🚀 Model Hub Monitor</h3>

<div id="newmodels"></div>

</div>


<div id="panel" class="panel"></div>

<script>

let signals=[
"HIGH VOLATILITY",
"BULLISH TREND",
"BEARISH SIGNAL",
"POSITIVE SENTIMENT"
]

let models=[
"ETH Volatility Predictor",
"Crypto Sentiment AI",
"Market Regime Detector",
"BTC Price Predictor"
]


function addEvent(){

let m=models[Math.floor(Math.random()*models.length)]
let s=signals[Math.floor(Math.random()*signals.length)]

let time=new Date().toLocaleTimeString()

let text="["+time+"] "+m+" generated "+s

let feed=document.getElementById("feed")

let div=document.createElement("div")

div.className="event"

div.innerText=text

feed.prepend(div)

if(feed.children.length>8){

feed.removeChild(feed.lastChild)

}

}

setInterval(addEvent,3000)


function addModel(){

let m=models[Math.floor(Math.random()*models.length)]

let time=new Date().toLocaleTimeString()

let text="["+time+"] new model detected → "+m

let box=document.getElementById("newmodels")

let div=document.createElement("div")

div.className="event"

div.innerText=text

box.prepend(div)

if(box.children.length>6){

box.removeChild(box.lastChild)

}

}

setInterval(addModel,7000)



function showModel(name,signal,confidence,desc){

let panel=document.getElementById("panel")

panel.style.display="block"

panel.innerHTML="<h2>"+name+"</h2>"
+"<p><b>Signal:</b> "+signal+"</p>"
+"<p><b>Confidence:</b> "+confidence+"%</p>"
+"<p>"+desc+"</p>"
+"<div class='timeline'>Signal timeline generated</div>"
+"<div class='close' onclick='closePanel()'>Close</div>"

}

function closePanel(){

document.getElementById("panel").style.display="none"

}

</script>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
