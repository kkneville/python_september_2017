from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	
	return render_template("index.html", redval = 255, greenval= 255, blueval = 255)

	
@app.route("/", methods=["POST"])	
def coloredindex():
	
	return render_template("index.html", redval = request.form["red"], greenval= request.form["green"], blueval = request.form["blue"])

app.run(debug=True)