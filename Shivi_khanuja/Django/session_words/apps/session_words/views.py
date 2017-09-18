from django.shortcuts import render, redirect
from django .contrib import messages

def index(request):
    return render(request,'session_words/index.html')

def create (request):
    #step 1:validations
   
    if request.method == "POST":
        print request.POST
        if request.POST ["word"] == "":
            messages.error(request, 'Word cannot be Empty')
            return redirect ('/')

    #step2:figure out what was selected



    
        
  
 