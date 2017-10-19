from flask import Flask, request, redirect, render_template, session, flash
from datetime import datetime
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')

import md5, os, binascii
password = 'password'

app.secret_key = 'secret_key'

def validate_registration(form_data):
    errors = []
    if len('name') < 2:
        errors.append('need longer name')
    if len('username') < 2:
        errors.append('need longer username')
    if len('password') < 3:
        errors.append('need longer password')
    if 'confirm_password' != 'password':
        errors.append('confirmation doesnt match password')



# Name
# Username
# Password:
# Password Confirmation
# Date of Birth

def login_validation():
    if len('username') < 2:
        errors.append('need longer username')
    if len('password') < 3:
        errors.append('need longer password')
# Username
# Password

@app.route("/")
def home():
    return render_template("login_registration.html")

@app.route("/process", methods = ["POST"])
# print request.form
def process():
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(request.form['password'] + salt).hexdigest()
    query = "INSERT INTO users(name, username, password, appointment_date, created_at, updated_at, salt) VALUES(:name, :username, :password, :appointment_date, now(), now(), :salt)"
# the data library needs to be in the same order
    data = {
        'name': request.form['name'],
        'username': request.form['username'],
        'password': hashed_pw,
        'appointment_date': request.form['appointment_date'],
        'salt': salt,

    }
    print '**************',mysql.query_db(query, data)
    print '&&&&&&&&&&&&',request.form['appointment_date']
    # print what the user put in the form
    # date = datetime.strptime(request.form['appointment_date'], '%Y-%m-%d')
    # # putting the user data into the string parseDDDD time func with default date format
    # date_string = date.strftime('%b %d, %y')
    # # variable equals a date string in the format that you want
    # current_date = datetime.now()
    # # makes the current date
    #
    # print date_string
    # if date > current_date:
    #     # if the date is greater then that means the number is higher/its in the future (vice versa)
    #     errors.append("Are you from the future?")

    return redirect("/index")

@app.route("/index")
def index():
    return render_template("friends.html")

app.run(debug=True)
