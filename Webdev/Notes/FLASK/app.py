from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
admin = True

@app.route("/")
def home():
    return render_template("index.html", heading="Home Page", content="")

@app.route("/test")
def testing():
    return render_template("index.html", heading="Test page", content="This is not a drill!")

@app.route("/admin")
def administrator():
    if admin:
        return "You are an administrator"
    else:
        return redirect(url_for("home"))

@app.route("/<name>")
def hello(name):
    return f"Hello {name}!"



app.run()