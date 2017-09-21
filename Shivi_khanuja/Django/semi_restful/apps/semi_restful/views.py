from django.shortcuts import render, redirect

def index(request):
    return render (request,'semi_restful/index.html')


def new(request):
    print "hello new page"
    return render(request,'semi_restful/new.html')
