from django.shortcuts import render, redirect, reverse
from .models import User
from django.contrib import messages
# Create your views here.
def flash_errors(req, errors, tag):
	for error in errors:
		messages.add_message(req, messages.ERROR, error, extra_tags=tag)
	pass

def current_user(req):
	return User.objects.get(id=req.session['user_id'])
	
def index(req): 
	return render(req, "login_registration/index.html")

def success(req):
	if not 'user_id' in req.session:
		return redirect(reverse('landing'))
	context = {
		"user":current_user(req),
		}

	return render(req, "login_registration/success.html", context)	

def login(req):
	if req.method == 'POST':
		result = User.objects.validate_login(req.POST)
		
		if not 'errors' in result:
			req.session['user_id'] = result['user'].id
			return redirect(reverse('dashboard'))
		
		flash_errors(req,result['errors'], "login")
	
	return redirect(reverse('landing'))

def logout(req):
	if 'user_id' in req.session:
		req.session.pop('user_id')
	return redirect(reverse('landing'))
	
def register(req):
	if req.method == "POST":
		#validate form data
		errors = User.objects.validate_registration(req.POST)
		
		#check for errors not exist
		if not errors:
			#create user
			user = User.objects.create_user(req.POST)
			#log in
			req.session['user_id'] = user.id
			
			#redirect to sucess
			return redirect(reverse('dashboard'))
		
		#flash error
		flash_errors(req, errors, "registration")
		
		#redirect landing
	return redirect(reverse('landing'))