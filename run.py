
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/tortoises.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", tortoises=data)


@app.route("/about/<tort_name>")
def about_tort(tort_name):
    tort = {}
    with open("data/tortoises.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == tort_name:
                tort = obj
    return render_template("tort.html", tort=tort)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/shop")
def shop():
    return render_template("shop.html", page_title="Shop")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
