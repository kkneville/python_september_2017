from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Wish, User
# Create your views here.

def flash_errors(errors, request):
    print '*****youre in the flash_errors method*****'

    for error in errors:
        messages.error(request, error)


def current_user(request):
    print '*****youre in the current_user method*****'

    if 'user_id' in request.session:
        User.objects.get(id=request.session['user_id'])

def dashboard(request):
    print'*****youre in the dashboard method *****'
    context = {
        # 'current_user' : User.objects.current_user(request)
    'current_user' : current_user(request)
    }
    return render(request, 'wish_app/dashboard.html', context)

def wish_item(request):
    print'*****youre in the wish_item method *****'
    return render(request, 'wish_app/create.html')

def create_item(request):
    print'*****youre in the create_item method *****'
    if request.method == 'POST':
        errors = Wish.objects.validate_wish(request.POST)
        if not errors:
            user = User.objects.current_user(request)
            wish = Wish.objects.create_wish(request.POST, user)
            return redirect(reverse('dashboard'))
        flash_errors(request, error)
    return redirect(reverse('create_item'))

def remove_wish(request, id):
    thisItem = Item.objects.get(id=id)
    user = User.objects.currentUser(request)
    user.wished_items.remove(thisItem)
    return redirect ('/dashboard')

def delete_wish(request, id):
    Wish.objects.get(id=id).delete()
    return redirect(reverse('dashboard'))

def show_wish(request, id):

    return render(request, wish_items.html)

def delete_wish(request, id):
    return redirect ('/dashboard')

def remove_wish(request, id):
    wish = wish.objects.get(id=id)

    return redirect ('/dashboard')

def add_wish(request, id):
    return redirect ('/dashboard')
