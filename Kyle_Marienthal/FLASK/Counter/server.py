from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)

app.secret_key = "this_is_a_secret"

@app.route("/")
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template('index.html', count = session['count'])

@app.route('/doubled')
def count_two():
    session['count'] +=1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('count')
    session['count']=0
    return redirect('/')




app.run(debug=True)
