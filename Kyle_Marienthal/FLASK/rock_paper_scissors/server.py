from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
import random
app.secret_key = 'secret_key'

def comp_choice():
    arr = ['rock', 'paper', 'scissors']
    return arr[random.randrange(0,3)]

def result(user,comp):
    if user == comp:
        session['tie'] += 1
        return 'tie'
    if user == 'rock':
        if comp == 'scissors':
            session['win'] += 1
            return 'win'
        else:
            session['lose'] += 1
            return 'lose'
    if user == 'paper':
        if comp == 'rock':
            session['win'] += 1
            return 'win'
        else:
            session['lose'] += 1
            return 'lose'
    if user == 'scissors':
        if comp == 'paper':
            session['win'] += 1
            return 'win'
        else:
            session['lose'] += 1
            return 'lose'
# session['win'] += 1
# session['lose'] += 1
# print result('rock',comp_choice())

@app.route("/")
def index():
    if 'win' not in session:
        session['win'] = 0
    print session['win']
    if 'lose' not in session:
        session['lose'] = 0
    print session['lose']
    if 'tie' not in session:
        session['tie'] = 0
    print session['tie']
    return render_template("index.html", win = session['win'], lose = session['lose'], tie = session['tie'])


@app.route('/selection', methods = ['POST'])
def select():
    outcome = result(request.form.keys()[0],comp_choice())
    print outcome
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.pop('win')
    session['win'] = 0
    session.pop('tie')
    session['tie'] = 0
    session.pop('lose')
    session['lose'] = 0
    return redirect('/')





# @app.route('/selection', methods=["POST"])
# def ():
#
#  return redirect('/')



app.run(debug=True)
