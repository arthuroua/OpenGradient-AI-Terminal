from flask import Flask
import random

app = Flask(__name__)

models = [
("ETH Volatility Predictor","Predict ETH volatility using GARCH"),
("Crypto Sentiment AI","Analyze market sentiment"),
("Market Regime Detector","Detect bull/bear regimes"),
("BTC Price Predictor","Forecast BTC price trends"),
("DeFi Risk Analyzer","Analyze DeFi protocol risk"),
("AI Trading Agent","Autonomous crypto trading AI"),
("Portfolio Optimizer","Optimize crypto portfolios"),
("Onchain Data Analyzer","Analyze blockchain activity"),
("Liquidity Predictor","Predict market liquidity"),
("Gas Fee Estimator","Estimate Ethereum gas fees")
]

signals = [
"Bullish",
"Bearish",
"High Volatility",
"Positive Sentiment",
"Risk Increase"
]

@app.route("/")
def home():

    cards=""

    for name,desc in models:

        confidence=random.randint(60,95)
        signal=random.choice(signals)

        size=confidence*2

        if confidence > 80:
            color="#16c784"
        elif confidence > 70:
            color="#f3ba2f"
        else:
            color="#ea3943"

        cards+=f"""

        <div class="tile"
        onclick="showModel('{name}','{signal}','{confidence}','{desc}');addWatch('{name}')"
        style="width:{size}px;height:{size}px;background:{color};">

        <div class="tile-title">{name}</div>
        <div class="tile-signal">{signal}</div>
        <div class="tile-score">{confidence}%</div>

        </div>

        """

    html=f"""

<html>

<head>

<title>OpenGradient AI Terminal</title>

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
font-weight:bold;
background:linear-gradient(90deg,#00f2ff,#8a5cff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}}

.subtitle{{opacity:0.6;}}

.container{{
max-width:1200px;
margin:auto;
padding:20px;
}}

.heatmap{{
display:flex;
flex-wrap:wrap;
gap:10px;
justify-content:center;
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

.tile-title{{font-weight:bold;margin-bottom:4px}}
.tile-score{{font-size:16px;font-weight:bold;margin-top:4px}}

.legend{{
display:flex;
justify-content:center;
gap:20px;
margin-top:20px;
}}

.box{{width:14px;height:14px;border-radius:3px}}
.green{{background:#16c784}}
.yellow{{background:#f3ba2f}}
.red{{background:#ea3943}}

.activity{{
max-width:800px;
margin:40px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
}}

.event{{border-bottom:1px solid #1c233a;padding:6px 0}}

.panel{{
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
background:#0f1424;
padding:30px;
border-radius:12px;
width:320px;
display:none;
border:1px solid #1c233a;
box-shadow:0 0 25px rgba(0,242,255,0.15);
}}

.timeline{{
margin-top:15px;
background:#05070d;
padding:10px;
border-radius:8px;
font-size:13px;
}}

.timeline-item{{
border-bottom:1px solid #1c233a;
padding:6px 0;
}}

.close{{cursor:pointer;margin-top:10px;color:#00f2ff}}

.watchlist{{
max-width:800px;
margin:30px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
}}

.watch-item{{
border-bottom:1px solid #1c233a;
padding:6px 0;
}}

</style>

</head>

<body>

<div class="header">

<div class="title">OpenGradient AI Terminal</div>
<div class="subtitle">AI Model Signals Dashboard</div>

</div>

<div class="container">

<div class="heatmap">

{cards}

</div>

<div class="legend">

<div><div class="box green"></div> Strong</div>
<div><div class="box yellow"></div> Neutral</div>
<div><div class="box red"></div> Weak</div>

</div>

</div>


<div class="watchlist">

<h2>⭐ Model Watchlist</h2>

<div id="watchlist"></div>

</div>


<div class="activity">

<h2>⚡ Live Model Activity</h2>

<div id="feed"></div>

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
box.innerHTML+=`<div class="watch-item">⭐ ${m}</div>`
}})
}}

const models=[
"ETH Volatility Predictor",
"Crypto Sentiment AI",
"Market Regime Detector",
"BTC Price Predictor",
"DeFi Risk Analyzer",
"AI Trading Agent"
]

const signals=[
"HIGH VOLATILITY",
"BULLISH TREND",
"BEARISH SIGNAL",
"POSITIVE SENTIMENT",
"RISK INCREASE"
]

function addEvent(){{
let model=models[Math.floor(Math.random()*models.length)]
let signal=signals[Math.floor(Math.random()*signals.length)]
let time=new Date().toLocaleTimeString()
let event=`[${{time}}] ${{model}} generated ${{signal}}`
let feed=document.getElementById("feed")
let div=document.createElement("div")
div.className="event"
div.innerText=event
feed.prepend(div)
if(feed.children.length>10){{feed.removeChild(feed.lastChild)}}
}}

setInterval(addEvent,3000)

function generateTimeline(){{

let signals=[
"HIGH VOLATILITY",
"BULLISH TREND",
"BEARISH SIGNAL",
"POSITIVE SENTIMENT",
"RISK INCREASE"
]

let html=""

for(let i=0;i<5;i++){{

let time=new Date(Date.now()-i*60000).toLocaleTimeString()

let signal=signals[Math.floor(Math.random()*signals.length)]

html+=`
<div class="timeline-item">
${{time}} — ${{signal}}
</div>
`

}}

return html

}}

function showModel(name,signal,confidence,desc){{

let panel=document.getElementById("panel")

panel.style.display="block"

panel.innerHTML=`

<h2>${{name}}</h2>

<p><b>Signal:</b> ${{signal}}</p>

<p><b>Confidence:</b> ${{confidence}}%</p>

<p><b>Description:</b><br>${{desc}}</p>

<h3>Signal Timeline</h3>

<div class="timeline">
${{generateTimeline()}}
</div>

<div class="close" onclick="closePanel()">Close</div>

`

}}

function closePanel(){{
document.getElementById("panel").style.display="none"
}}

</script>

</body>

</html>

"""

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
