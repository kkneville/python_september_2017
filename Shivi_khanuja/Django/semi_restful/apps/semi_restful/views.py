from django.shortcuts import render, redirect, reverse
from .models import User

def index(request):
    context = {
        'users' : User.objects.all()
    }
    return render (request,'semi_restful/index.html',context)


def new(request):
    print "hello new page"
    return render(request,'semi_restful/new.html')

def create(request):
    if request.method == "POST":
        pass

        errors = User.objects.validate(request.POST)

        if errors:
            pass

        user = User.objects.create_user(request.POST)    
        

        # print reverse('show_user', kwargs = {'id': user.id})
        return redirect(reverse('show_user', kwargs= {'id': user.id}))

    return redirect(reverse('new_user'))    

def show(request ,id ):
    user = User.objects.get(id = id)

    context = {
        'user' : user,
    }

    return render(request, 'semi_restful/show.html', context)

