from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(response):
	response = "placeholder to display all the surveys created"
	return HttpResponse(response)

def survey(response):
	response = "placeholder for users to add a new survey"
	return HttpResponse(response)