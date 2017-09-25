from django.shortcuts import render, redirect, reverse
from .models import CreditCard, User

def index(request):
    context = {
        'user': User.objects.current_user(request)
    }

    return render(request, 'credit_card_app/index.html', context)

def add(request):

    return render(request, 'credit_card_app/add.html')

def create(request):
    if request.method == "POST":

        credit_card = CreditCard.objects.createCreditCard(request, request.POST)

        return redirect(reverse('all_credit_cards'))

    return redirect(reverse('add_credit_card'))
