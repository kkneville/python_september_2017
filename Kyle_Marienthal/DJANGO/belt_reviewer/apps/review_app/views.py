from django.shortcuts import render, redirect, reverse
from ..book_app.models import Book
from ..log_reg_app.models import User
from .models import Review
from django.contrib import messages

# Create your views here.
def current_user(request):
    print '*****book_app current_user method*****'

    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])

def flash_errors(request, errors):
    for error in errors:
        messages.error(request, error)


def index(request):
    print '*****youre in the index method of review app*****'
    context = {
        'current_user': current_user(request)
    }

    return redirect(reverse( 'add_book' ))

def create_review(request):
    print '*****review_app create_review method*****'
    if request.method == "POST":
    # validate the form data
        errors = Review.objects.validate(request.POST)
    # if no errors
        book = Book.objects.filter(id=request.POST['book_id']).first()
        if not errors:
        # get current_user
            user = current_user(request)
        # get the current book
        # create the review
        # create your own create_review(request.POST, book, user) method in the modelManager to make things cleaner
            review = Review.objects.create_review(request.POST, book, user)
        # redirect to book show page: in order to show a specific book you need to include the book id and kwargs is how you have to do it. this lets you put the id in the url
        # youll need to create the show_book url next
            return redirect(reverse('show_book', kwargs={'id': book.id}))
    # if errors flash the errors and redirect to the current page
    flash_errors(request, errors)
    return redirect(reverse('show_book', kwargs={'id': book.id}))

# def add_book(request):
#     print '*****youre in the add_book method of review app*****'
#     return redirect(reverse('book_info'))
