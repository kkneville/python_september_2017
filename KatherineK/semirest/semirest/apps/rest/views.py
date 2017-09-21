from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from .models import *
import random, re


def all(request):
    context = {
        "users": User.objects.all(),
    }
    return render(request, "rest/all.html", context)

def new(request):
    if "errors" not in request.session:
        request.session['errors'] = []
    else :
        errors = request.session['errors']
        request.session['errors'] = []
    context = {
        "errors": errors, 
    }
    return render(request, "rest/new.html", context)

def create(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if errors:
            request.session['errors'] = errors
            return redirect('/new')
        user = User.objects.create_user(request.POST)
    return redirect(reverse('show', kwargs = {'id':user.id}))

def show(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user,
    }
    return render(request, "rest/user.html", context)

def edit(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user,
    }
    return render(request, "rest/edit.html", context)

def edit_user(request, id):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if errors:
            request.session['errors'] = errors
            return redirect(reverse('edit', kwargs = {'id':user.id}))
    id = request.POST['id']
    user = User.objects.edit(request.POST)
    return redirect(reverse('show', kwargs = {'id':user.id}))

def delete(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user,
    }
    return render(request, "rest/delete.html", context)

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')
