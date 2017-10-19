from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)

app.secret_key = "kk%^8Xa!BF6BULy5a3nXFgZW%Q^W5uZ7*6*T2$*#FA"
 
@app.route("/")
def index():
	if 'activities' not in session:
		session['activities'] = []
	if 'gold' not in session:
		session['gold'] = 0
	return render_template("index.html", activities = session['activities'], gold= session['gold'])

@app.route('/process_money', methods=["POST"])
def process():
	#FARM FARM FARM FARM FARM
	if request.form['building']=="farm":
		num = random.randrange(10, 21)
		session['gold'] += num
		session['activities'].append("Earned " + str(num) + " gold from the farm! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
	
	#CAVE CAVE CAVE CAVE CAVE
	elif request.form['building']=="cave":
		num = random.randrange(5, 11)
		session['gold'] += num
		session['activities'].append("Earned " + str(num) + " gold from the cave! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
	
	#HOUSE HOUSE HOUSE HOUSE HOUSE
	elif request.form['building']=="house":
		num = random.randrange(2, 6)
		session['gold'] += num
		session['activities'].append("Earned " + str(num) + " gold from home! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")

	#CASINO CASINO CASINO CASINO
	else:
		num = random.randrange(-50, 51)
		session['gold'] += num
		if num > 0:
			session['activities'].append("Entered a casino and won " + str(num) + " gold! Lucky! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
		elif num < 0:
			session['activities'].append("Entered a casino and lost "+ str(num) + " gold... Ouch.. ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
		else:
			session['activities'].append("Entered a casino and broke even ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")")
	return redirect('/')

@app.route("/new", methods=['POST'])
def new():
	session.pop("activities")
	session.pop("gold")
	
	return redirect('/')




app.run(debug=True) 
