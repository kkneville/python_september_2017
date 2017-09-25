# Still not working:
# 2 - unable to clear session data with clear button/reset Function




# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *

def index(request):
    if "entries" not in request.session :
        request.session['entries'] = []
    entries = request.session['entries']
    context = {
        "entries": entries,
    }
    return render(request, "words/index.html", context)

def add(request):

    date = strftime("%m-%d-%Y", gmtime())
    time = strftime("%H:%M:%S", gmtime())
    if len(request.POST['word']) < 1 :
        return redirect('/')
    else :
        word = request.POST['word']

    classes = ""
    classes += (request.POST['style'])
    if "color" in request.POST :
        classes += (request.POST['color'])
    else:
        classes += "black "
    if "large" in request.POST :
        classes += "large "
    else :
        classes += "small "

    entry = {
        "date": date,
        "time": time,
        "word": word,
        "classes": classes,
    }

    entries = request.session['entries']
    entries.insert(0,entry)
    request.session['entries'] = entries

    return redirect('/')

def reset(request):
    print 'sanity check'
    del request.session['entries']
    # request.session.flush()
    # request.session.pop("entries")
    # request.session['entries'] = []
    # for key in request.session.keys():
    #     del request.session[key]

    return redirect('/')
