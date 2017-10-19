from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import md5, os, binascii

app = Flask(__name__)
app.secret_key = "mysupersecretkey"
mysql = MySQLConnector(app, 'loginandregister')

def validate_registration(form_data):
    errors = {}

    # First Name
    if len(form_data['first_name']) == 0:
        errors['first_name'] = "First name is required."
    # Last Name
    if len(form_data['last_name']) == 0:
        errors['last_name'] = "Last name is required."
    # Email
    if len(form_data['email']) == 0:
        errors['email'] = "Email is required."
    # Password
    if len(form_data['password']) == 0:
        errors['password'] = "Password is required."
    # Password Confirmation
    if 'password_confirmation' in form_data:
        if form_data['password'] != form_data['password_confirmation']:
            errors['password_confirmation'] = "Passwords do not match."

    return errors

def validate_login(form_data):
    errors = {}

    # Email
    if len(form_data['email']) == 0:
        errors['email'] = "Email is required."
    # Password
    if len(form_data['password']) == 0:
        errors['password'] = "Password is required."

    user = get_user(email=form_data['email'])

    # If user with email exists
    if user != []:
        print 'user', user
        user = user[0]
        hashed_pw = md5.new(form_data['password'] + user['salt']).hexdigest()
        # password do not match
        if user['password'] != hashed_pw:
            errors['password'] = "Did you forget your password?"
    # Email is not in database
    else:
        errors['email'] = "You must register first."

    return errors

def flash_errors(errors, type):
    for input, error in errors.iteritems():
        flash(error, type)

def create_user(form_data):
    salt =  binascii.b2a_hex(os.urandom(15)) 
    hashed_pw = md5.new(form_data['password'] + salt).hexdigest()

    query = """
        insert into users (first_name, last_name, email, password, salt, created_at, updated_at)
        values (:first_name, :last_name, :email, :password, :salt, now(), now())
    """

    data = {
        'first_name': form_data['first_name'],
        'last_name': form_data['last_name'],
        'email': form_data['email'],
        'password': hashed_pw,
        'salt': salt,
    }

    return mysql.query_db(query, data)

def get_user(**kwargs):
    column = kwargs.iterkeys().next()   
    query = "select id, first_name, last_name, email, salt, password, created_at from users where {} = :value".format(column)
    data = {
        'value': kwargs[column]
    }

    return mysql.query_db(query, data)

@app.route('/')
def index():
    print "Inside the index method."

    return render_template('index.html', errors = [])

@app.route('/register', methods=["POST"])
def register():
    #Validate my form data
    errors = validate_registration(request.form)

    #if there are errors
    if errors:
        #flash error messages 
        flash_errors(errors, 'register') 
        #redirect to the index
        return redirect('/')

    #Create the user
    user_id = create_user(request.form)
   
    #redirect success
    flash("Successfully Registered. Please login to continue!", 'register')
    return redirect('/')

@app.route('/login', methods=["POST"])
def login():
    #validate the form data
    errors = validate_login(request.form)

    #if errors exist
    if errors:
        #flash the errors
        flash_errors(errors, 'login')
        #redirect to the index
        return redirect('/')

    #log in the user
    user = get_user(email=request.form['email'])[0]
    session['user_id'] = user['id']

    #redirect to success
    return redirect('/success')

@app.route('/success')
def success():
    user = get_user(id = session['user_id'])

    return render_template('success.html', user=user[0])

app.run(debug=True)







