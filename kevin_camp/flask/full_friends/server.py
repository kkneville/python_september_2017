from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, now(), now())"
	data = {
		'name': request.form['name'],
		'age': request.form['age'],
	}
	mysql.query_db(query,data)
	return redirect('/')

app.run(debug=True)
