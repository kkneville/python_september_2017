from django.shortcuts import render, redirect
from datetime import datetime
from time import gmtime, strftime

def index(request):
	context = {
	"time_date": datetime.now().strftime("%I:%M %p %m-%d-%Y")
	}
	return render(request, 'time_display/index.html', context)
