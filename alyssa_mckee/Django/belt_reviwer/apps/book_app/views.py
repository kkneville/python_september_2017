from django.shortcuts import render, redirect, reverse
from ..login_registration.models import User
from ..review_app.models import Review
from .models import Book, Author
from django.contrib import messages
#from ..login_registration.views import current_user
# Create your views here.

def flash_errors(req, errors, tag=""):
	for error in errors:
		messages.add_message(req, messages.ERROR, error, extra_tags=tag)
	print("flash")
		
def index(req): #dashboard
	if not 'user_id' in req.session:
		return redirect(reverse('landing'))
	
	user = User.objects.get_user(req.session['user_id'])
	reviews = Review.objects.all().order_by('-id')[:3]
	books = Book.objects.all()
	context = {
		"user": user[0],
		"reviews": reviews,
		"books": books,
	}
	
	
	return render(req, "book_app/index.html", context)
	
def show(req, id):
	if not 'user_id' in req.session:
		return redirect(reverse('landing'))
	book = Book.objects.filter(id=id)
	if not book.exists():
		return redirect(reverse("dashboard"))
	
	
	context = {
		"book":book[0],
		"reviews": list(book[0].reviews.all()),
		
	}
	
	return render(req, "book_app/book.html", context)
	
def add(req):
	if not 'user_id' in req.session:
		return redirect(reverse('landing'))
	authors = Author.objects.all()
	content = {"authors":[]}
	for author in authors:
		content['authors'].append(author)
		
	return render(req,"book_app/new.html", content)
	
def create(req):
	if not 'user_id' in req.session:
		return redirect(reverse('landing'))
	if not req.method == "POST":
		return redirect(reverse('add_book'))
	
	print(req.POST)
	
	bookerrors = Book.objects.validate_book(req.POST)
	
	authorerrors = Author.objects.validate_author(req.POST)

	reviewerrors = Review.objects.validate_review(req.POST)	
	
	#if errors
	if authorerrors or bookerrors or reviewerrors:
		flash_errors(req, bookerrors,"bookerrors" )
		flash_errors(req, authorerrors, "authorerrors")
		flash_errors(req, reviewerrors, "reviewerrors")
		return redirect(reverse("add_book"))
	
	#create author, book, and review
	book = Book.objects.create_book(req.POST)
	
	review = Review.objects.create_review(req.POST, book)
	
	return redirect(reverse("dashboard"))