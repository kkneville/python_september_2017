from flask import Flask, render_template, request, redirect, flash
import re

app = Flask(__name__)

app.secret_key="bRjeWr*C7AVGg6@PUhu46a#qwrYJXxu9Vs25JrKhVn"

@app.route("/")
def index():
	return render_template("index.html")

@ app.route("/result", methods=['POST'])
def process():
	if len(request.form['name']) == 0:
		flash("please enter a name")
		return redirect('/')
	if not request.form['name'].isalpha():
		flash("please enter a valid name")
		return redirect('/')
	if len(request.form['comment']) > 120:
		flash("message must be under 120 characters")
		return redirect('/')
	name = request.form['name']
	comment = request.form['comment'] if len(request.form['comment']) != 0 else "no comment"
	language = request.form['language']
	location = request.form['location']
	return render_template("result.html", name=name, location=location, language=language, comment=comment)
	
app.run(debug=True)