from django.shortcuts import render, redirect, reverse
from ..login_registration_app.models import User
from .models import Membership

def index(request):

    return render(request, 'membership_app/index.html')

def create(request):
    if request.method == "POST":
        user = User.objects.current_user(request)

        membership = Membership.objects.create_membership(request.POST, user)

    return redirect(reverse('all_services'))

def remove(request, id):
    membership = Membership.objects.filter(id=id).first()
    user = User.objects.current_user(request)

    if membership and membership.user == user:
        membership.delete()

    return redirect(reverse('all_services'))