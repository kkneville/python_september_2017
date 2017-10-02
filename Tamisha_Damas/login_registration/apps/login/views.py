from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
# Create your views here.
def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)

def current_user(request):
    return User.objects.get(id = request.session['user_id'])

def index(request):
    print "index"
    return render(request, 'login/index.html')

def success(request):
    if 'user_id' in request.session:
        context = {
            'user': current_user(request),
        }
        return render(request, 'login/success.html', context)
    return redirect(reverse('landing'))

def register(request):
    if request.method == "POST":
        #Validate form data
        errors = User.objects.validate_registration(request.POST)
        #Check if errors don't exist
        if  not errors:
            #create User
            user = User.objects.create_user(request.POST)
            #log in the User
            request.session['user_id'] = user.id
            #redirect to success page
            return redirect(reverse('dashboard'))
        #Flash errors
        flash_errors(errors, request)

        print request.POST

    return redirect(reverse('landing'))

def login(request):
    if request.method == "POST":
        #validate my login data
        check = User.objects.validate_login(request.POST)

        if check['user']:
            #log in user
            request.session['user-id'] = check['user'].id
            #redirect to succes page
            return redirect(reverse('dashboard'))
        #flash error messages
        flash_errors(check['errors'], request)

    return redirect(reverse('landing'))
    # print "login"
    # return render(reverse('login'))

def logout(request):
    if 'user-id' in request.session:
        request.session.pop('user_id')

    return redirect(reverse('landing'))
