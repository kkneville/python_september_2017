# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *

def index(request):
    date = strftime("%Y-%m-%d", gmtime())
    time = strftime("%H:%M:%S", gmtime())
    print get_random_string(length=14)
    context = {
        "date": date,
        "time": time
    }
    return render(request, "datetimeapp/index.html", context)
