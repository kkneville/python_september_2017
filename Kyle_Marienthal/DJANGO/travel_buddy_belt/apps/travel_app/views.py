# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from ..log_reg_app.models import User
from .models import Trip

# Create your views here.
def flash_errors(errors, request):
    print '*****log_reg flash_errors method*****'

    for error in errors:
        messages.error(request, error)

def current_user(request):
    print '*****travel current_user method*****'

    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

def success(request):
    print '*****youre in the travel success method*****'
    context = {
        'current_user': current_user(request),
    }
    return render(request, 'travel_app/success.html', context)

def add_trip(request):
    print '***** youre in the travel add_trip method*****'
    context = {
        'current_user' : current_user(request)
    }
    return render(request, 'travel_app/add_trip.html', context)

def create_trip(request, ):
    print '***** youre in the travel create_trip method*****'

    if request.method == "POST":
        errors = Trip.objects.trip_input_validator(request.POST)
        if not errors:
            trip = Trip.objects.create_trip(request.POST)

    return redirect(reverse('dashboard'))
