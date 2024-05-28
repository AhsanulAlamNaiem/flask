from flask import Flask, redirect, url_for, render_template, request, session, flash
import json
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=13)

@app.route("/")
def home():
    return(render_template("home.html"))

@app.route("/login",methods =["POST","GET"])
def login():
    if request.method =="POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return(redirect(url_for("user")))
        else:
            return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return(redirect(url_for("login")))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        flash("your have been loged out","info")
        return(f"<h1>{user}</h>")
    else:
        return(redirect(url_for("login")))


# if __name__ =="__main__":
#     app.run(port=8080, host = "0.0.0.0")