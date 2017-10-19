from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector 
import re
import sys

def log(obj):
	print(obj, file=sys.stderr)

NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')

app = Flask(__name__)
app.secret_key="Mo!W6s1nG@e545$9j9OnEpyuBK*&M@X*l1HBORF3&I"

mysql = MySQLConnector(app, 'facelessbook_db') 

@app.route("/")
def index():
	query = '''SELECT CONCAT_WS(' ', first_name, last_name) AS name, age, DATE_FORMAT(created_at, "%M %e") AS date, YEAR(created_at) AS year FROM friends'''
	log(mysql.query_db(query))
	data = mysql.query_db(query)
	return render_template("index.html", data=data)

@app.route('/process', methods=["POST"])
def process():
	log(request.form)
	error = False
	if len(request.form['first_name']) == 0:
		flash("Please enter a first name")
		error = True
	if not NAME_REGEX.match(request.form['first_name']):
		flash("First name is invalid")
		error = True
	if len(request.form['last_name']) == 0:
		flash("Please enter a last name")
		error = True
	if not NAME_REGEX.match(request.form['last_name']):
		flash("Last name is invalid")
		error = True
	if len(request.form['age']) == 0:
		flash("please enter an age")
		error = True
	elif not request.form['age'].isdigit():
		flash("age must be a number")
		error = True
	elif int(request.form['age']) < 0:
		flash("Age is invalid")
		error = True
	
	if error:
		return redirect("/")
	
	query = '''INSERT INTO friends(first_name, last_name, age, created_at) VALUES(:first_name, :last_name, :age, now())'''
	data = {"first_name":request.form["first_name"],"last_name":request.form["last_name"], "age":request.form["age"]}
	mysql.query_db(query, data)
	return redirect('/')

	
	
app.run(debug=True) 
