from flask import Flask, flash, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

# Global Game Options
OPTIONS = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'spock': 4,
}

# Instantiate session default values
def sessionDefaults():
    if 'wins' not in session:
        session['wins'] = 0
    if 'losses' not in session:
        session['losses'] = 0
    if 'ties' not in session:
        session['ties'] = 0
    if 'total' not in session:
        session['total'] = 0

# Random option value ('rock', 'paper', 'scissors')
def randomOption():
    return random.choice(OPTIONS.keys())

# Game Logic
# @player str param
# @computer str param
def roshambo(player, computer):
    output = {}
    diff = OPTIONS[computer] - OPTIONS[player]
    message = "The computer picked {} and you picked {}, you {}!"
    print computer, player, diff
    if diff == 0:
        result = "tie"
        session['ties'] += 1
    # two win condtions to account on four options
    elif diff % 4 == 1 or diff % 4 == -1:
        result = "lose"
        session['losses'] += 1
    elif diff % 4 == 2 or diff % 4 == 3:
        result = "win"
        session['wins'] += 1

    return {
        'message': message.format(computer, player, result),
        'result': result
    }

# Landing Page
@app.route('/')
def index():
    print "Inside the index method."
    sessionDefaults()

    return render_template('index.html')

# Process User Selection
# @user_choice str param in ('rock', 'paper', 'scissors')
@app.route('/process/<user_choice>')
def process(user_choice):
    print "Inside the process method."

    if user_choice in OPTIONS:
        comp_choice = randomOption()

        outcome = roshambo(user_choice, comp_choice)
        flash(outcome['message'])
        session['total'] += 1

    return redirect('/')

# Clear Session
@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')

app.run(debug=True)