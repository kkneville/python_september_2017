from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
from ..review_app.models import Review
# Create your views here.

def flash_errors(errors, request):
    print '*****log_reg flash_errors method*****'

    for error in errors:
        messages.error(request, error)

def index(request):
    print '*****log_reg index method*****'

    return render(request, 'log_reg_app/index.html')

def current_user(request):
    print '*****log_reg current_user method*****'

    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

def register(request):
    print '*****log_reg register method*****'

    if request.method == 'POST':
        errors = User.objects.validate_registration(request.POST)
        # the validate_registration function returns a list of errors
        if not errors:
            # create the user
            user = User.objects.create_user(request.POST)
            # create_user function returns a whole user object
            # now log them in by making their id accessible from session
            request.session['user_id'] = user.id
            # redirect to success page
            return redirect(reverse('dashboard'))
        flash_errors(errors, request)
        # the errors argument is supplied by the validate_registration function
    return redirect(reverse('landing'))

def login(request):
    print '*****log_reg login method*****'

    if request.method == 'POST':
        # validate the login data
        check = User.objects.validate_login(request.POST)
        # check if you got a user
        if 'user' in check:
            # log them in
            request.session['user_id'] = check ['user'].id
            #then redirect to success page
            return redirect(reverse('dashboard'))
        #  if there is no user flash the errors you collect with flash_errors and send them back to the landing page
        flash_errors(check['errors'], request)

    return redirect(reverse('landing'))

def logout(request):
    print "*****log_reg logout method*****"
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect(reverse('landing'))

def success(request):
    # this method is no longer used because you added other apps this used to take you to the dead
    # success page
    print '*****log_reg success method*****'

    return redirect(reverse('dashboard'))

def user_info(request, id):
    titles = Review.objects.user_book_reviews(id)
    context = {
    'current_user':current_user(request),
    'titles' : titles
    }
    return render(request, 'log_reg_app/user_info.html', context)
