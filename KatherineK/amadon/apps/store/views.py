from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
import random

def index(request):
    return render(request, "store/index.html" )

def process(request):

    request.session['item'] = request.POST['item']
    request.session['quantity'] = float(request.POST['quantity'])
    request.session['price'] = float(request.POST['price'])*float(request.session['quantity'])

    if "count" not in request.session:
        request.session['count'] = request.session['quantity']
    else :
        request.session['count'] += request.session['quantity']

    if "total" not in request.session:
        request.session['total'] = request.session['price']
    else :
        request.session['total'] += request.session['price']


    return redirect('/checkout')

def checkout(request):

    item = request.session['item']
    quantity = request.session['quantity']
    price = request.session['price']
    count = request.session['count']
    total = request.session['total']

    context = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "count": count,
        "total": total,
    }

    return render(request, "store/checkout.html", context)

def reset(request):
    return redirect('/')
