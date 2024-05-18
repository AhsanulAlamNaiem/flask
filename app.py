from flask import Flask, redirect, url_for, render_template,send_file

app = Flask(__name__)

@app.route("/")

def home():
    return(render_template("home.html"))

@app.route("/<name>")
def portfolio(name):
    return(render_template("portfolio.html"))

@app.route("/admin")

def admin():
    return(render_template("admin.html"))  

@app.route("/kaizen")
def kaizen():
    file="res/kaizen SUST.pptx"
    return( send_file(file,as_attachment=True))

if __name__ =="__main__":
    app.run(debug = True, port=8080, host = "0.0.0.0")