from django.shortcuts import render, redirect

def index(request):
    return render(request,'login/index.html')

def register(request):
    if request.method== POST:
        
        return render(request,'login/index.html')    

def login(request):
    if request.method== POST:
    
        return render(request,'login/index.html')    
