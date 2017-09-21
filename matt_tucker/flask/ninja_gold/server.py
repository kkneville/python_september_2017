from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)

app.secret_key = "secret"

# Buildings with their gold ranges
buildings = {
    'farm': [10, 20],
    'cave': [5, 10],
    'house': [2, 5],
    'casino': [-50, 50],
}

# Instantiate default session keys and values
def default_session():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []


# Update gold value in session
# @param gold INT
def update_gold(gold):
    session['gold'] += gold


# Add a new activity to session
# @param gold INT
# @param building STRING
def add_activity(gold, building):
    if gold > 0:    # Won gold
        text_color = "green"
        message = "You entered a {} and won {} golds!".format(building, gold)
    elif gold < 0:  # Lost Gold
        text_color = "red"
        message = "Enter a casino and lost {} golds... ouch...".format(gold)
    else:           # Broke Even
        text_color = "grey"
        message = "You entered a casino and broke even... phew..."

    activity = {'message': message, 'color': text_color}

    session['activities'].insert(0, activity) # Prepend activity to activities

# Default Index Page
@app.route('/')
def index():
    default_session() # Instantiate default session keys

    return render_template('index.html', gold=session['gold'], activities=session['activities'])

# Handle POST request for building
# @param building ROUTE PARAMETER
@app.route('/process_money/<building>', methods=['POST', 'GET'])
def process_money(building):
    if building in buildings:   # Check if route param is a valid building
        amounts = buildings[building] # Retrieve the buildings gold range
        gold = random.randint(amounts[0], amounts[1]) # Random amount of gold

        update_gold(gold) # Update session gold value
        add_activity(gold, building) # Update session activites value

    return redirect('/')

# Reset the game
@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('activities')

    return redirect('/')

app.run(debug=True)