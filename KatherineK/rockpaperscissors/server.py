import random, md5, re
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'roshambodb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def front():
    return render_template('front.html')

@app.route('/game')
def game():
    # print mysql.query_db('select * from players')
    if "response" not in session:
        session['response'] = ""
    if "wins" not in session:
        session['wins'] = ""
    if "losses" not in session:
        session['losses'] = ""
    if "ties" not in session:
        session['ties'] = ""
    return render_template('index.html', response=session['response'], wins=session['wins'], losses=session['losses'], ties=session['ties'])

@app.route('/play', methods=['POST'])
def play():
    data = 0
    query= "select * from players where idplayers = 1"
    player = mysql.query_db(query)[0]
    print player

    computerplay = random.randrange(1, 4)
    print computerplay

    button = int(request.form['button'])

    if button == computerplay :
        data = player['ties'] + 1
        session["ties"] = data
        query= '''UPDATE players
                set ties = :result
                where idplayers = 1'''
        session['response'] = "It's a tie!"

    elif (button == 1 and computerplay == 3) or (button == 2 and computerplay == 3) or (button == 3 and computerplay == 1) :
        data = player['losses'] + 1
        session["losses"] = data
        query= '''UPDATE players
                set losses =:result
                where idplayers = 1'''
        session['response'] = "You lost."

    elif (button == 1 and computerplay == 2) or (button == 2 and computerplay == 1) or (button == 3 and computerplay == 2) :
        data = player['wins'] + 1
        session["wins"] = data
        query= '''UPDATE players
                set wins =:result
                where idplayers = 1'''
        session['response'] = "You won."

    print query
    print data
    print mysql.query_db(query, {'result': data})
    return redirect ('/game')

@app.route('/reset', methods=["post"])
def reset():
    query= '''UPDATE players
            set losses = 0
            where idplayers = 1'''
    mysql.query_db(query)

    query= '''UPDATE players
            set wins = 0
            where idplayers = 1'''
    mysql.query_db(query)

    query= '''UPDATE players
            set ties = 0
            where idplayers = 1'''
    mysql.query_db(query)

    session["ties"] = 0
    session["losses"] = 0
    session["wins"] = 0

    return redirect ('/game')

@app.route('/users/create', methods=['POST'])
def create_user():
    if len(request.form['username']) < 1 :
        flash("Please enter a username")
        return redirect ('/')
    else :
        username = request.form['username']
    if not EMAIL_REGEX.match(request.form['email']):
            flash("Please enter a valid email address")
            return redirect ('/')
    else :
        email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()

    insert_query = "INSERT INTO players (username, email, password, created_at, updated_at) VALUES (:username,:email, :password, NOW(), NOW())"
    query_data = { 'username': username, 'email': email, 'password': password }
    mysql.query_db(insert_query, query_data)

    return redirect ("/game")


@app.route('/users/login', methods=['POST'])
def login_user():
        username = request.form['username']
        password = md5.new(request.form['password']).hexdigest()
        user_query = "SELECT * FROM players where players.username = :username AND players.password = :password"
        query_data = { 'username': username, 'password': password}
        user = mysql.query_db(user_query, query_data)
        if len(user) < 1 :
            flash("Unable to locate user. Please register below.")
            return redirect ('/')
        return redirect ("/game")

app.run(debug=True)
