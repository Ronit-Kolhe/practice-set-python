from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    request.form
    with open (  )
    return render_template("contact.html")

app.run(debug = True)