from flask import Flask
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

# сигнали для UI
signals = [
"Bullish",
"Bearish",
"High Volatility",
"Positive Sentiment"
]

# отримуємо реальні моделі з Model Hub
def get_models():

    try:

        url = "https://hub.opengradient.ai"

        r = requests.get(url, timeout=6)

        soup
