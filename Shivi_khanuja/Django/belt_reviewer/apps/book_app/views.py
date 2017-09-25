from django.shortcuts import render, redirect, reverse

def index(request):
    return render(request, 'book_app/index.html')

def add(request):
    return render(request, 'book_app/add.html')

