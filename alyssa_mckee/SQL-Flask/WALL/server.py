from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector 
import sys, re

def log(obj, *args):
	print(obj, file=sys.stderr)
	for arg in args:
		print(arg, file=sys.stderr)
#--------------------------------------

app = Flask(__name__)
app.secret_key = "don't forget the secret key"

mysql = MySQLConnector(app, 'thewall') 

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
	errors = validate_login(request.form)
	if errors:
		for error in errors:
			flash(error, "login_error")
		return redirect('/')
	
	
	query = "SELECT id FROM users WHERE email = :email"
	data = {"email": request.form['email']}
	user_id = mysql.query_db(query, data)[0]['id']
	
	#log the user in
	session['user_id'] = user_id 
	
	return redirect('/wall')

@app.route('/register', methods=["POST"])
def register():
	errors = validate_registration(request.form)
	if errors:
		for error in errors:
			flash(error,"registration_error")
		log("errors found")
		return redirect('/')
	log("no errors found")
	
	query = '''INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
					VALUES (:first_name, :last_name, :email, :password, now(), now())'''
	data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email'], 'password': request.form['password']}
	
	#log the user in
	session['user_id'] = mysql.query_db(query, data)
	
	return redirect('/wall')

def validate_registration(data):
	# errors = {}
	errors = []
	
	first_name = data['first_name']
	last_name = data['last_name']
	email = data['email'].lower()
	password = data['password']
	c_password = data['confirm_password']
	
	#first_name
	if len(first_name) < 2:
		errors.append("first name must be greater than 2 characters")
		# errors['first_name'] = ["first name must be greater than 2 characters"]
	if not first_name.isalpha():
		errors.append("first name can not contain numbers or special characters")
		# if 'first_name' not in errors:
			# errors['first_name'] = []
		# errors['first_name'].append("first name can not contain numbers or special characters")
	
	#last_name
	if len(last_name) < 2:
		errors.append("first name must be greater than 2 characters")
		# errors['last_name'] = ["last name must be greater than 2 characters"]
	if not last_name.isalpha():
		errors.append("last name can not contain numbers or special characters")
		# if 'last_name' not in errors:
			# errors['last_name'] = []
		# errors['last_name']append("last name can not contain numbers or special characters")
		
		
	#email
	query = "SELECT COUNT(email) AS count FROM users WHERE email = :email"
	data = {"email": email}
	result = mysql.query_db(query, data)
	if result[0]['count'] != 0:
		errors.append("Email Taken")
		# errors['email'] = ["Email Taken"]
	
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
	if len(email) == 0:
		errors.append("Email is required")
		# if 'email' not in errors:
			# errors['email'] = []
		# errors['email'].append("Email is required")
	
	if not EMAIL_REGEX.match(email):
		errors.append("Not a valid email")
		# if 'email' not in errors:
			# errors['email'] = []
		# errors.append("Not a valid email")
	
	
	#password
	if len(password)<8:
		errors.append("Password must be at least 8 characters.")
		# errors['password'] = ["Password must be at least 8 characters."]
	if password != c_password:
		errors.append("Password does not match")
		# if 'password' not in errors:
			# errors['password'] = []
		# errors['password'].append("Password does not match")

	return errors

def validate_login(data):
	errors = []
	
	email = data['email']
	password = data['password']
	
	if len(email) == 0:
		errors.append("Email is required")
	
	if len(password)== 0:
		errors.append("Password is required")
	
	query = "SELECT COUNT(email) AS count FROM users WHERE email = :email"
	data = {"email": email}
	result = mysql.query_db(query, data)
	if result[0]['count'] == 0:
		errors.append("Account not found")
		return errors
	
	query = "SELECT password FROM users WHERE email = :email"
	data = {"email": email}
	stored_password = mysql.query_db(query, data)[0]['password']
	if password != stored_password:
		errors.append("Incorrect password")
	return errors
	
@app.route('/wall')
def wall():
	#technically you'd also need to make sure that user_id is in the database?
	if 'user_id' not in session:
		flash("Nice Try! You must login to view THE WALL", "rejected")
		return redirect('/')
	
	name = mysql.query_db("SELECT first_name FROM users WHERE id = {}".format(session['user_id']) )
	
	#get messages from database
	query = '''SELECT CONCAT_WS(' ', users.first_name, users.last_name) AS name, DATE_FORMAT(messages.created_at, "%M %e %Y") AS post_date, messages.content AS content, messages.id AS id FROM users
		JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC'''
	message_list = mysql.query_db(query)
	
	#get comments from database
	query = '''SELECT CONCAT_WS(' ', users.first_name, users.last_name) AS name, DATE_FORMAT(comments.created_at, '%M %e %Y') AS post_date, comments.content AS content, comments.message_id AS message_id FROM users 
JOIN comments ON comments.user_id = users.id 
ORDER BY comments.created_at ASC'''
	comment_list = mysql.query_db(query)
	
	return render_template('wall.html', messages = message_list,comments = comment_list, name = name)

@app.route('/post_message', methods=["POST"])
def post_message():
	content = request.form['content']
	if len(content) == 0:
		flash("Message can not be empty", "alert")
		return redirect('/wall')
	
	query = '''INSERT INTO messages (content, created_at, updated_at, user_id) VALUES(:content, now(), now(), :user_id)'''
	data={"content": content, "user_id": session['user_id']}
	mysql.query_db(query, data)
	
	return redirect('/wall')

@app.route('/post_comment', methods=["POST"])
def post_comment():
	content = request.form['content']
	if len(content) == 0:
		flash("comment can not be empty", "alert")
		return redirect('/wall')
	
	message_id = request.form['message_id']
		
	query = '''INSERT INTO comments (content, created_at, updated_at, user_id, message_id) VALUES(:content, now(), now(), :user_id, :message_id)'''
	data={"content": content, "user_id": session['user_id'], "message_id": message_id}
	mysql.query_db(query, data)
	
	return redirect('/wall')
	
@app.route('/logout')
def logout():
	session.pop('user_id')
	return redirect('/')

app.run(debug=True) 
