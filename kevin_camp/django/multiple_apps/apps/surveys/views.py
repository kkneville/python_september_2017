from django.shortcuts import render, HttpResponse, redirect

def index(request):
	comment = "placeholder to display all the surveys created"
	return HttpResponse(comment)

def new(request):
	comment = "placeholder for users to add a new survey"
	return HttpResponse(comment)
