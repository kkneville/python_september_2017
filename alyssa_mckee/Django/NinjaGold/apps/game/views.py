from django.shortcuts import render, redirect
import random
from datetime import datetime
# Create your views here.
def index(req):
	if 'activities' not in req.session:
		req.session['activities'] = []
	if 'gold' not in req.session:
		req.session['gold'] = 0
	
	return render(req, "game/index.html")
	
def process(req):
	#FARM FARM FARM FARM FARM
	if req.POST['building']=="farm":
		num = random.randrange(10, 21)
		req.session['gold'] += num
		req.session['activities'].insert(0,{"color": "green","message":"Earned " + str(num) + " gold from the farm! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")"})
	
	#CAVE CAVE CAVE CAVE CAVE
	elif req.POST['building']=="cave":
		num = random.randrange(5, 11)
		req.session['gold'] += num
		req.session['activities'].insert(0,{"color": "green","message":"Earned " + str(num) + " gold from the cave! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")"})
	
	#HOUSE HOUSE HOUSE HOUSE HOUSE
	elif req.POST['building']=="house":
		num = random.randrange(2, 6)
		req.session['gold'] += num
		req.session['activities'].insert(0,{"color": "green","message":"Earned " + str(num) + " gold from home! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")"})

	#CASINO CASINO CASINO CASINO
	else:
		num = random.randrange(-50, 51)
		req.session['gold'] += num
		if num > 0:
			req.session['activities'].insert(0,{"color": "green","message":"Entered a casino and won " + str(num) + " gold! Lucky! ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")"})
		elif num < 0:
			req.session['activities'].insert(0,{"color": "red","message":"Entered a casino and lost "+ str(num) + " gold... Ouch.. ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")"})
		else:
			req.session['activities'].insert(0,{"color": "black","message":"Entered a casino and broke even ("+ datetime.now().strftime('%Y/%m/%d %I:%M%p') + ")"})
	return redirect('/ninjagold/game')

def new(req):
	req.session.pop("activities")
	req.session.pop("gold")
	
	return redirect('/ninjagold/game')