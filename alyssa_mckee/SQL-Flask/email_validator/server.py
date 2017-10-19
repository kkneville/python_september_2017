from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector 
import sys
import re

def log(obj):
	print(obj, file=sys.stderr)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key="himitsu"
mysql = MySQLConnector(app, 'mydb') 

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
	if len(request.form['email']) == 0:
		flash("email can not be empty")
		return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']):
		flash("not a valid email")
		return redirect('/')
	
	mysql.query_db("INSERT INTO users(email, created_at) Values(:email, now())", {"email": request.form['email']})
	return redirect('/success')

@app.route('/success')
def sucess():
	data = mysql.query_db("SELECT id, email, DATE_FORMAT(created_at, '%m/%e/%y %l:%i %p') AS date FROM users")
	
	return render_template("success.html", data = data)

@app.route('/delete', methods=['POST'])
def delete():
	id = int(request.form['id'])
	mysql.query_db("DELETE FROM users WHERE id = :id", {"id": id })
	return redirect('/success')
app.run(debug=True) 
