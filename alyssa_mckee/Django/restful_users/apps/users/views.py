from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
	users = User.objects.all()
	context = {"users":users}
	return render(req, "users/index.html", context)

def new(req):
	#show edit form
	context = {}
	if 'errors'in req.session:
		context["errors"] = req.session['errors']
		context["data"]=req.session['create_data']
		req.session.pop('create_data')
		req.session.pop('errors')
	return render(req, "users/new_user.html", context)

def edit(req, id):
	#show edit form
	user = User.objects.filter(id=id)
	if len(user) == 0: #if user doesn't exist
		return redirect(reverse("all_users"))
	user = user[0]
	context = {
		"first_name":user.first_name,
		"last_name":user.last_name,
		"email": user.email,
		"id": user.id,
	}
	if 'errors' in req.session:
		context["errors"] = req.session['errors']
		req.session.pop('errors')
	
	return render(req, "users/edit_user.html", context)

def show(req, id):
	#show the users profile
	user = User.objects.filter(id=id)
	if len(user) == 0:
		return redirect(reverse("all_users"))
	user = user[0]
	context = {
		"first_name":user.first_name,
		"last_name":user.last_name,
		"email": user.email,
		"id": user.id,
		"created_at": user.created_at
	}
	return render(req, "users/profile.html", context)
	
def create(req):
	#handles new user post request
	data = req.POST
	errors = User.objects.validate(data)
	if errors:
		req.session['errors'] = errors
		req.session['create_data'] = data
		return redirect(reverse("new_user"))
	user = User.objects.create_user(data)
	
	return redirect(reverse("show_user", kwargs={'id':user.id}))
	
def destroy(req, id):
	user = User.objects.filter(id=id)
	if len(user) != 0: #if user exists, then destroy them. mercilously
		User.objects.destroy(id)
	
	return redirect(reverse("all_users"))

def update(req, id):
	data = req.POST
	errors = User.objects.validate(data)
	if errors:
		req.session['errors'] = errors
		return redirect(reverse("edit", kwargs={'id':id}))
	user = User.objects.edit_user(data)
	return redirect(reverse("show_user", kwargs={'id':user.id}))
	