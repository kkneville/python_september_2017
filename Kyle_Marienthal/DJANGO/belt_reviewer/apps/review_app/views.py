from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request):
    print '*****youre in the index method of review app*****'
    return render(request, 'review_app/review.html')
