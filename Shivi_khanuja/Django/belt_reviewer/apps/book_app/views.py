from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from ..reviews.models import Review
from .models import Book

def current_user(request):
    return User.objects.get(id=request.session['user_id'])

def flash_errors(request, errors):
    for error in errors:
        messages.error(request, error)
    

def index(request):
    
    books = Book.objects.all()
    


    context = {
        'user' : current_user(request),
        'books': books,
    }
    return render(request, 'book_app/index.html',context)

def add(request):
    return render(request, 'book_app/add.html')

def create (request):
    if request.method == "POST":
        errors = Book.objects.validate(request.POST)

        if not errors:
            
            user = current_user(request)
            
            book = Book.objects.create_book(request.POST)
            if len(request.POST['content']) > 1:

                review = Review.objects.create_review(request.POST, book ,user)
        
            return redirect(reverse('show_book',kwargs={'id' : book.id}))

        
    return redirect(reverse('add_book'))    
def show(request, id):
    context= {
        'book' : Book.objects.get(id=id),
    }
    return render(request,'book_app/show.html',context)
