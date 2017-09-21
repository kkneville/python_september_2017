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

def all_works(request):
    works = Work.objects.all()
    context = {
        "works": works,
    }
    return render(request, "works/allworks.html", context)

def new_work(request):
    if "errors" not in request.session:
        request.session['errors'] = []
    else :
        errors = request.session['errors']
        request.session['errors'] = []

    users = User.objects.all()
    context = {
        "users": users,
        "errors": errors,
    }
    return render(request, "works/new_work.html", context)

def create_work(request):
    errors = Work.objects.validate(request.POST)
    if errors:
        request.session['errors'] = errors
        return redirect('/new_work')
    work = Work.objects.create_work(request.POST)
    return redirect(reverse('show_work', kwargs = {'workid':work.id}))

def show_work(request, workid):
    work = Work.objects.get(id=workid)
    context = {
        "work": work,
    }
    return render(request, "works/show_work.html", context)

def show_author_work(request, id):
    works = Work.objects.all().filter(author=id)
    user = User.objects.get(id=id)
    context = {
        "works": works,
        "user": user,
    }
    return render(request, "works/show_author_work.html", context)

def worksedit(request, workid):
    work = Work.objects.get(id=workid)
    user = work.author
    context = {
        "work": work,
        "user": user,
    }
    print work
    print user
    return render(request, "works/edit_work.html", context)

def edit_work(request):
    errors = Work.objects.validate(request.POST)
    if errors:
        request.session['errors'] = errors
        return redirect(reverse('show_work', kwargs = {'workid':work.id}))
    work = Work.objects.edit(request.POST)
    return redirect(reverse('show_work', kwargs = {'workid':work.id}))

def worksdelete(request):
    pass

def delete_work(request):
    pass
