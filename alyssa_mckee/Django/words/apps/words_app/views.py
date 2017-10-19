from django.shortcuts import render, redirect
from time import localtime, strftime
# Create your views here.
def index(request):
	return render(request, "words_app/index.html")

def process(request):
	if not 'words' in request.session:
		request.session['words'] = []
	
	if not 'word' in request.POST:
		return redirect('/session_words')
	
	word_data = {
		"word": request.POST['word'],
		"color": request.POST['color'],
		"time": strftime('%I:%M:%S%p, %b %d',localtime()) + num_extention(strftime('%d',localtime())) + strftime(' %Y',localtime())
	}
	if 'size' in request.POST:
		word_data['size'] = True

	request.session['words'].append(word_data)
	
	return redirect('/session_words')

def clear(request):
	request.session.pop('words')
	
	return redirect("/session_words")
	pass
	
def num_extention(num):
	num = int(num)
	if 10< num and num < 20:
		return "th"
	if num % 10 == 1:
		return "st"
	if num % 10 == 2:
		return "nd"
	if num % 10 == 3:
		return "rd"
	return "th"