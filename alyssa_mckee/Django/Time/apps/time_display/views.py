from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime
# Create your views here.
def index(request):
	context = {
		"time":strftime("%I:%M %p",localtime()),
		"date":strftime("%b %d, %Y",localtime()),
	}
	
	return render(request, "time_display/index.html", context)