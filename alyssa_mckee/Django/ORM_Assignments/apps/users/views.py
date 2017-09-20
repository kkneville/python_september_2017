from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(req):

	return HttpResponse("Success!")