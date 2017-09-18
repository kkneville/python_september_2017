from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "survey_app/index.html")
	
def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	
	return redirect("/result")

def result(request):
	return render(request, "survey_app/result.html")