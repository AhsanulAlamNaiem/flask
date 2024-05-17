from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return("<a href = 'https://www.google.com'>Hi</a>")