from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    marks = {
        "Ronit" : "45",
        "Arjun" : "69",
        "Shubhum" : "54",
        "Ritesh" : "90"




    }
    return render_template("index.html",marks = marks)

app.run(debug  = True)
