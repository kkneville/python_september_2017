from flask import Flask, render_template, session, request, redirect
import random
import sys

app = Flask(__name__)

app.secret_key = "Fhm$x3e6!b!AbfDy521Q0TQ@xu3KVBKc7nc&7^$HY2"

@app.route("/")
def index():
	if 'message' not in session:
		session['message'] = ""
	if 'color' not in session:
		session['color'] = "red"
	if 'show_alert' not in session:
		session['show_alert'] = False
	if 'allow_guess' not in session:
		session['allow_guess'] = True
	if 'play_again' not in session:
		session['play_again'] = False

	if 'random' not in session:
		session['random'] = random.randrange(0, 101)
	return render_template("index.html", message=session['message'], color=session['color'], show_alert=session['show_alert'], allow_guess=session['allow_guess'], play_again=session['play_again'])

@app.route("/process", methods=['POST'])
def process():
	if request.form['action'] == "guess":
		session['show_alert'] = True
		session['allow_guess'] = True
		session['color'] = "red"
		if int(request.form['number']) > session['random']:
			session['message'] = "Too High!"
		elif int(request.form['number']) < session['random']:
			session['message'] = "Too Low!"
		else: #its equal :)
			session['message'] = str(session['random']) + " was the number!"
			session['color'] = "limegreen"
			session['show_alert'] = True
			session['play_again'] = True
			session['allow_guess'] = False

	if request.form['action'] == "again":
		session.clear()
	return redirect('/')

app.run(debug=True)