from flask import Flask, redirect, url_for, render_template,send_file
from flask_talisman import Talisman
import json

app = Flask(__name__)
# Talisman(app)

@app.route("/")
def home():
    return(render_template("home.html"))

@app.route("/admin")
def admin():
    return(render_template("admin.html"))  

@app.route("/kaizen_data_version")
def kaizen():
    file="res/dataversion.json"
    with open(file,"r") as f:
        data = json.load(f)

    return(str(data["currentversion"]))

@app.route("/members")
def members():
    file="res/memberDB.json"
    return( send_file(file,as_attachment=True))
@app.route("/committee")
def committee():
    file="res/committeeDB.json"
    return( send_file(file,as_attachment=True))
@app.route("/advisors")
def advisors():
    file="res/advisorsDB.json"
    return( send_file(file,as_attachment=True))

if __name__ =="__main__":
    app.run(port=8080, host = "0.0.0.0")