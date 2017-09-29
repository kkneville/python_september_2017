from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Trip, User
# Create your views here.
# if request.method == "POST":
# context = {
# 'current_user' : current_user(request)
# }
def flash_errors(errors, request):
    print '*****youre in the flash_errors method*****'

    for error in errors:
        messages.error(request, error)

def current_user(request):
    print '*****youre in the current_user method*****'

    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

def dashboard(request):
    print '***** youre in the travel dashboard method*****'
    trips = Trip.objects.all()
    other_users = {User.objects.all().exclude(id=current_user(request).id)}
    context = {
        'current_user' : current_user(request),
        'trips' : trips,
        'other_users' : other_users
    }
    return render(request, 'travels_app/dashboard.html', context)

def add_trip(request):
    print '***** youre in the travel add_trip method*****'
    context = {
        'current_user' : current_user(request)
    }
    return render(request, 'travels_app/add_trip.html', context)

def create_trip(request):
    print '***** youre in the travel create_trip method*****'
    user = current_user(request)
    trips = Trip.objects.create_trip(request.POST, user)
    return redirect(reverse('dashboard'))

def destination(request, id):
    context = {
        'current_user' : current_user(request)

    }
    return render(request, 'travels_app/destination.html', context)
