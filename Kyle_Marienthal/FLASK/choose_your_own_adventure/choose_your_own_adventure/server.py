from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/left")
def left():
    return render_template("left.html")

@app.route("/right")
def right():
    return render_template("right.html")

@app.route("/Reddoor")
def Reddoor():
    return render_template("Reddoor.html")

@app.route("/TBD")
def TBD():
    return render_template("TBD.html")

@app.route('/life')
def life():
    return redirect('/')

@app.route('/work')
def work():
    return render_template('work.html')

app.run(debug=True)
