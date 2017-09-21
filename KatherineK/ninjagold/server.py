import random
from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)

app.secret_key = "secret"

@app.route('/', methods=['GET', 'POST'])
def index():
    if "goldcount" not in session :
        session['goldcount'] = 0
    if "gold" not in session :
        session['gold'] = 0
    if "activity" not in session :
        session['activity'] = ""
    if "earned" not in session :
        session['earned'] = ""
    if "log" not in session :
        session['log'] = []



    return render_template("index.html", goldcount=session['goldcount'], log=session['log'])



@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['button'] == "farm":
        session['gold'] = random.randrange(10,21)
        session['activity'] = request.form['button']
    if request.form['button'] == "cave":
        session['gold'] = random.randrange(5,11)
        session['activity'] = request.form['button']
    if request.form['button'] == "house":
        session['gold'] = random.randrange(2,6)
        session['activity'] = request.form['button']
    if request.form['button'] == "casino":
        session['gold'] = random.randrange(-50,51)
        session['activity'] = request.form['button']
    session['goldcount'] += session['gold']
    if session['gold'] > 0 :
        session['earned'] = "earned"
    else :
        session ['earned'] = "lost"

    earned=session['earned']
    gold=session['gold']
    location=session['activity']

    entry = {
        "gold": gold,
        "location": location,
        "earned": earned,
    }

    session['log'].append(entry)

    return redirect ("/")

@app.route('/reset', methods=['POST'])
def reset():
    session['goldcount'] = 0
    session['gold'] = 0
    session.pop('log')
    return redirect ("/")


app.run(debug=True)
