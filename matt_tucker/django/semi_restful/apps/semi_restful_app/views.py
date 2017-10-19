from django.shortcuts import render, redirect, reverse
from .models import User

def index(request):
    print "Inside the index method."

    context = {
        'users': User.objects.all()
    }

    return render(request, 'semi_restful_app/index.html', context)

def new(request):
    print "Inside the new method."

    return render(request, 'semi_restful_app/new.html')

def create(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)

        if errors:
            pass # flash errors

        user = User.objects.create_user(request.POST)

        return redirect(reverse('show_user', kwargs = {'id': user.id}))

    return redirect(reverse('new_user'))

def show(request, id):
    user = User.objects.get(id = id)

    context = {
        'user': user,
    }

    return render(request, 'semi_restful_app/show.html', context)





