from flask import Flask
import random

app = Flask(__name__)

models = [
("ETH Volatility Predictor","Predict ETH volatility"),
("Crypto Sentiment AI","Analyze market sentiment"),
("Market Regime Detector","Detect bull/bear regimes"),
("BTC Price Predictor","Forecast BTC trends"),
("DeFi Risk Analyzer","Analyze DeFi risk"),
("AI Trading Agent","Autonomous crypto trading AI"),
("Portfolio Optimizer","Optimize crypto portfolios")
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

        if confidence>80:
            color="#16c784"
        elif confidence>70:
            color="#f3ba2f"
        else:
            color="#ea3943"

        safe=name.replace("'","")

        cards += """
        <div class='tile'
        onclick="showModel('{0}','{1}','{2}','{3}');addWatch('{0}')"
        style='width:{4}px;height:{4}px;background:{5};'>

        <div class='tile-title'>{0}</div>
        <div>{1}</div>
        <div class='tile-score'>{2}%</div>

        </div>
        """.format(safe,signal,confidence,desc,size,color)

    html = """
<!DOCTYPE html>
<html>
<head>

<title>OpenGradient AI Terminal</title>

<style>

body{
background:#05070d;
color:white;
font-family:Arial;
margin:0;
}

.header{
text-align:center;
padding:40px;
}

.title{
font-size:42px;
font-weight:bold;
color:#00f2ff;
}

.heatmap{
display:flex;
flex-wrap:wrap;
gap:10px;
justify-content:center;
padding:20px;
}

.tile{
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
}

.tile:hover{
transform:scale(1.1);
}

.tile-title{
font-weight:bold;
margin-bottom:4px;
}

.tile-score{
font-size:16px;
font-weight:bold;
margin-top:4px;
}

.panel{
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
background:#0f1424;
padding:20px;
border-radius:10px;
width:320px;
display:none;
}

.timeline{
margin-top:10px;
font-size:13px;
}

.activity{
max-width:700px;
margin:40px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
}

.event{
border-bottom:1px solid #1c233a;
padding:5px 0;
}

.watchlist{
max-width:700px;
margin:30px auto;
background:#0f1424;
padding:20px;
border-radius:10px;
}

.watch-item{
border-bottom:1px solid #1c233a;
padding:6px 0;
}

</style>

</head>

<body>

<div class="header">
<div class="title">OpenGradient AI Terminal</div>
</div>

<div class="heatmap">
""" + cards + """

</div>


<div class="watchlist">
<h3>⭐ Model Watchlist</h3>
<div id="watchlist"></div>
</div>


<div class="activity">
<h3>⚡ Live Model Activity</h3>
<div id="feed"></div>
</div>


<div class="activity">
<h3>🚀 Model Hub Monitor</h3>
<div id="monitor"></div>
</div>


<div id="panel" class="panel"></div>


<script>

let watchlist=[]

function addWatch(name){

if(!watchlist.includes(name)){
watchlist.push(name)
renderWatch()
}

}

function renderWatch(){

let box=document.getElementById("watchlist")

box.innerHTML=""

watchlist.forEach(m=>{
box.innerHTML+="<div class='watch-item'>⭐ "+m+"</div>"
})

}

const models=[
"ETH Volatility Predictor",
"Crypto Sentiment AI",
"Market Regime Detector",
"BTC Price Predictor"
]

const signals=[
"HIGH VOLATILITY",
"BULLISH TREND",
"BEARISH SIGNAL",
"POSITIVE SENTIMENT"
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


function monitorModel(){

let m=models[Math.floor(Math.random()*models.length)]

let time=new Date().toLocaleTimeString()

let text="["+time+"] new model detected → "+m

let box=document.getElementById("monitor")

let div=document.createElement("div")

div.className="event"

div.innerText=text

box.prepend(div)

if(box.children.length>6){
box.removeChild(box.lastChild)
}

}

setInterval(monitorModel,7000)



function generateTimeline(){

let html=""

for(let i=0;i<5;i++){

let time=new Date(Date.now()-i*60000).toLocaleTimeString()

let s=signals[Math.floor(Math.random()*signals.length)]

html+="<div class='event'>"+time+" — "+s+"</div>"

}

return html

}


function showModel(name,signal,confidence,desc){

let panel=document.getElementById("panel")

panel.style.display="block"

panel.innerHTML="<h2>"+name+"</h2>"
+"<p><b>Signal:</b> "+signal+"</p>"
+"<p><b>Confidence:</b> "+confidence+"%</p>"
+"<p>"+desc+"</p>"
+"<div class='timeline'>"+generateTimeline()+"</div>"
+"<button onclick='closePanel()'>Close</button>"

}

function closePanel(){
document.getElementById("panel").style.display="none"
}

</script>

</body>
</html>
"""

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
