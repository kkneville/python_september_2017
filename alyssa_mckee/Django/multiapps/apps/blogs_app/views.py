from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "placeholder to later display all the list of blogs"
	return HttpResponse(response)

def newblog(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(response):
	return redirect('/blogs')

def show(response, number):
	response = "placeholder to display blog " + number
	return HttpResponse(response)

def edit(response, number):
	response = "place holder to edit blog number " + number
	return HttpResponse(response)

def delete(response, number):
	return redirect('/blogs')