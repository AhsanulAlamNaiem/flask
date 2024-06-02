from flask import Flask, redirect, url_for, render_template, request, session, flash
import json, sqlite3
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=13)

conn= sqlite3.connect("./res/portfoliodb.db")

@app.route("/")
def home():
    db = sqlite3.connect('./res/portfoliodb.db')
    skills = db.execute("Select skill,skill_type from skills").fetchall()
    education = db.execute("Select Degree, startdate,  enddate, institute,description from education").fetchall()
    certificates = db.execute("Select tittle, date, skill, description from certificates").fetchall()
    services = db.execute("Select title, key from services").fetchall()
    services_list =[]
    for service in services:
        skills = db.execute("SELECT GROUP_CONCAT(skill, ', ') AS concatenated_skills FROM skills WHERE {service} = 1;".format(service = service[1])).fetchone()[0]
        services_list.append((service[0],skills))
    return(render_template("home.html",services = services_list,education=education, certificates = certificates))


if __name__ =="__main__":
    app.run(port=8080)