from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/ninjas")
def ninjas():
	return render_template("color.html", color="tmnt.png")

@app.route("/ninjas/<usercolor>")
def color(usercolor):
	if usercolor == "red" or usercolor== "orange"or usercolor== "blue" or usercolor== "purple":
		usercolor+=".jpg"
	else:
		usercolor="notapril.jpg"
	
	return render_template("color.html", color=usercolor)
	
app.run(debug=True)