from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector 
import re, os, binascii, hashlib, sys

def log(obj):
	print(obj, file=sys.stderr)


app = Flask(__name__)
app.secret_key = "ItsASecret"
mysql = MySQLConnector(app, 'mydb') 

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
	email = request.form['email'].lower()
	
	#validate email
	result = validator(email, "email")
	if not result['is_valid']:
		flash(result['response'], "login_error")
		return redirect('/')
		
	#check if user is in the database, if not, then add them
	temp = mysql.query_db("SELECT COUNT(id) AS count FROM users WHERE email = :email", {"email":email})
	
	#if email is not in database, account does not exist
	if temp[0]['count'] == 0:
		flash("account does not exist", "login_error")
		return redirect('/')
	
	#get users stored salt and password
	database_password = mysql.query_db("SELECT password FROM users WHERE email = :email", {"email": email})[0]['password']
	database_salt = mysql.query_db("SELECT salt FROM users WHERE email = :email", {"email": email})[0]['salt']
	
	#hash the users password with the user's salt
	password = hash_password(request.form['password'], database_salt)
	
	#check if passwords match
	result = validator([password, database_password], "password")
	if not result['is_valid']:
		flash("inncorrect password", "login_error")
		return redirect('/')
	
	#login success!, set name in session
	username = mysql.query_db("SELECT CONCAT_WS(' ', first_name, last_name) AS name FROM users WHERE email = :email", {"email": email})
	session['name'] = username[0]['name']

	return redirect('/success')
	
@app.route('/register', methods=["POST"])
def register():

	#validate first_name
	first_name = request.form['first_name']
	result = validator(first_name, "name")
	if not result["is_valid"]:
		flash("First name "+ result['response'], "registration_error")
		return redirect('/')	
	
	#validate last name
	last_name = request.form['last_name']
	result = validator(last_name, "name")
	if not result["is_valid"]:
		flash("Last name "+ result['response'], "registration_error")
		return redirect('/')
	
	#validate email
	email = request.form['email'].lower()
	result = validator(email, "email")
	if not result["is_valid"]:
		flash(result['response'], "registration_error")
		return redirect('/')
	
	#validate password
	result = validator(request.form['password'], request.form['confirm_password'], "password")
	if not result["is_valid"]:
		flash(result['response'], "registration_error")
		return redirect('/')
	
	#check if email already in database
	temp = mysql.query_db("SELECT COUNT(id) AS count FROM users WHERE email = :email", {"email":email})
	
	#if email is taken, flash the message, redirect to root
	if temp[0]['count'] != 0:
		flash("that email is taken", "registration_error")
		return redirect('/')
	
	#generate salt and hash the password
	salt = str(binascii.b2a_hex(os.urandom(15)))
	hashed_password = hash_password(password, salt)
	
	#insert user data into database
	query = '''INSERT INTO users(first_name, last_name, email, password, salt) 
	VALUES(:first_name, :last_name, :email, :password, :salt)'''
	data = {"first_name":first_name, "last_name":last_name, "email":email, "password": hashed_password, "salt": salt}
	mysql.query_db(query, data)
	
	
	#Registration success!
	username = mysql.query_db("SELECT CONCAT_WS(' ', first_name, last_name) AS name FROM users WHERE email = :email", {"email": email})
	session['name'] = username[0]['name']
	return redirect('/success')

@app.route('/success')
def success():
	return render_template("success.html", name = session['name'])

def validator(input, type):
	#result = {"result":True, "response":""}
	log("input")
	log(input)
	if type == "email":
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
		if len(input) == 0:
			return {"is_valid":False, "response":"Email is required."}
		if not EMAIL_REGEX.match(input):
			return {"is_valid":False, "response":"Not a valid email"}
		#email is valid
		return {"is_valid":True, "response":""}

	if type == "name":
		if len(input) < 2:
			return {"is_valid":False, "response":"must be 2 or more characters"}
		if not input.isalpha():
			return {"is_valid":False, "response":"can not contain numbers or special characters"}
		#name is valid
		return {"is_valid":True, "response":""}
		
	if type == "password":
		#password will be passed as an array. password in [0], confirm_password in [1]
		if len(input[0])<8:
			return {"is_valid":False, "response":"Password must be at least 8 characters."}
		if input[0] != input[1]:
			return {"is_valid":False, "response":"password does not match"}
		#password is valid
		return {"is_valid":True, "response":""}

def hash_password(pw, salt):
	salted_password = pw.encode() + salt.encode()
	return hashlib.md5(salted_password).hexdigest()


app.run(debug=True) 
