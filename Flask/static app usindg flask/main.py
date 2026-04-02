from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/designs")
def designs():
    return render_template("designs.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")
app.run(debug=True)