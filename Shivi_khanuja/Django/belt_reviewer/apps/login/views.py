from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User

def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)

def current_user(request):
    return User.objects.get(id=request.session['user_id'])


def index(request):
    return render(request,'login/index.html')

def success(request):
    if 'user_id' in request.session:
        context= {
            'user': current_user(request),
        }    
        return render(request,'login/success.html',context)
    return redirect(reverse('landing'))


def register(request):
    if request.method == "POST":
        #validate form data
        errors = User.objects.validate_registration(request.POST)

        #check if errors exit
        if not errors:
            user = User.objects.create_user(request.POST)
            
            
            request.session['user_id'] = user.id     
            
            return redirect(reverse('dashboard'))   
            
        flash_errors(errors, request)
        #flash error
        #redirect landing
        return redirect(reverse('landing'))    

def login(request):
    if request.method== "POST":
        
        check = User.objects.validate_login(request.POST)
        if check['user']:
            request.session['user_id'] = check['user'].id

            return redirect(reverse('dashboard'))
        flash_errors(check['errors'], request)
    
    return redirect(reverse('landing'))    

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect(reverse('landing'))

def show(request,id):
    user = User.objects.get(id=id)
    context = {
        'user':user,   
    }

    return render(request,'login/show.html',context)
