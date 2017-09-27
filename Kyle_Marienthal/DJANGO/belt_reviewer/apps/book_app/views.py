from django.shortcuts import render, reverse, redirect
from .models import Book
from ..log_reg_app.models import User
from ..review_app.models import Review
from django.contrib import messages

# Create your views here.
def current_user(request):
    print '*****book_app current_user method*****'

    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
def flash_errors(request, errors):
    for error in errors:
        messages.error(request, error)
def book(request):
    # print User.objects.all()
    reviews = Review.objects.all()
    newest_reviews = reviews.order_by('-created_at')[:3]
    context = {
        'current_user': current_user(request),
        'newest_reviews' : newest_reviews,
        'leftovers' : Review.objects.remaining_books()

    }
    print '*****youre in the success method of book_app*****'
    return render(request, 'book_app/books.html', context)

def book_info(request):
    print '*****book_app book_info method*****'
    return render(request, 'book_app/book_info.html')
def add_book(request):
    print '*****book_app add_book method*****'
    context = {
        'current_user': current_user(request)
    }
    return render(request, 'book_app/add_book.html', context)
def create_book(request):
    print '*****book_app create_book method*****'

    if request.method == "POST":
    # validate the form data
        errors = Book.objects.validate(request.POST)
    # if no errors
        if not errors:
        # get current_user
            user = current_user(request)
        # create the book
        # create your own create_book(request.POST) method in the modelManager to make things cleaner
            book = Book.objects.create_book(request.POST)
        # create the review
        # create your own create_review(request.POST, book, user) method in the modelManager to make things cleaner
            if len(request.POST['content']) > 1:
                    review = Review.objects.create_review(request.POST, book, user)

        # redirect to book show page: in order to show a specific book you need to include the book id and kwargs is how you have to do it. this lets you put the id in the url
        # youll need to create the show_book url next
            return redirect(reverse('show_book', kwargs={'id': book.id}))

    # if errors flash the errors and redirect to the current page
        flash_errors(request, errors)

    return redirect(reverse('add_book'))
def show_book(request, id):
    context = {
        'current_user' : current_user(request),
        'book' : Book.objects.get(id=id)
    }

    return render(request, 'book_app/show_book.html', context)
