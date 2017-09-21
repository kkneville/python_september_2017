# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("placeholder for later to display all surveys created")

def new(request):
    return HttpResponse("placeholder for users to add a new survey")# Create your views here.
