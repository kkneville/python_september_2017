from flask import Flask, render_template, redirect, request, session, flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)

app.secret_key = "Z%6QD3boMxk2M9xQ@oiq&5fRJB!A4A8*l#@!!y%4bX"

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
	error = False
	
	#VALIDATE FIRST NAME
	if len(request.form['first_name']) == 0:
		flash("please enter a first name")
		error = True
	elif not request.form['first_name'].isalpha():
		flash("first name can only contain letters")
		error = True
		
	#VALIDATE LAST NAME
	if len(request.form['last_name']) == 0:
		flash("please enter a last name")
		error = True
	elif not request.form['last_name'].isalpha():
		flash("last name can only contain letters")
		error = True
		
	#VALIDATE EMAIL
	if len(request.form['email']) == 0:
		flash("please enter an email")
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("please enter a valid email address")
		error = True
		
	#VALIDATE PASSWORD
	if not len(request.form['password']) > 8:
		flash("password must be more than 8 characters")
		error = True
	elif not request.form['password']==request.form['confirm_password']:
		flash("confirm password does not match")
		error = True
		
	#IF ERROR: REDIRECT
	if error:
		return redirect('/')
	
	#ELSE SUCCESS
	return render_template("success.html")
 
app.run(debug=True) 
