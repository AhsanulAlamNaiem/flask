from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return(render_template("home.html"))

@app.route("/<name>")
def portfolio(name):
    return(render_template("portfolio.html"))

@app.route("/admin")

def admin():
    return(redirect(url_for("home")))  