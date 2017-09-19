from django.shortcuts import render, redirect
from django .contrib import messages
from datetime import datetime

def index(request):
   
    if 'word_array' not in request.session:
        request.session['word_array'] = []
    print request.session['word_array']    
    return render(request,'session_words/index.html')

def create (request):
    #step 1:validations
   
    if request.method == "POST":
        print request.POST
        if request.POST ["word"] == "":
            messages.error(request, 'Word cannot be Empty')
            return redirect ('/')
        if 'color' not in request.POST:
            color = 'black'
        else:
            color = request.POST ['color']    
        if 'font' not in request.POST:
            font_size = 'default_font'
        else:
            font_size = 'large_font'        
            
        now = datetime.now()
        string_date = now.strftime("%d %m %Y")

        word = {
            'value': request.POST['word'],
            'color':  color,
            'font_size': font_size,
            'time': string_date
        }
        request.session['word_array'].append(word)
        
        request.session.modified=True
    return redirect ('/')

    #step2:figure out what was selected
def clear(request):
    if request.method == "POST":
        request.session.flush()
    return redirect ('/')


    
        
  
 