import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/checkpoint")
def checkpoint():
        return render_template("checkpoint.html")

@app.route("/cabinet_noir", methods=["POST"])
def cabinet_noir():
        error_message = None
        if request.method == "POST":
                if request.form["username"] != "demo" or request.form["password"] != "demo":
                        error_message = "Access denied."
                else:
                        return redirect(url_for("dashboard"))
        return render_template("checkpoint.html", error_message=error_message)

@app.route("/dashboard")
def dashboard():
        return render_template("dashboard.html")

if __name__ == "__main__":
        app.run(debug=True)
