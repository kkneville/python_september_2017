from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Review
from ..book_app.models import Book
def flash_errors(req, errors, tag=""):
	for error in errors:
		messages.add_message(req, messages.ERROR, error, extra_tags=tag)
# Create your views here.
def create(req):
	if req.method != "POST":
		return redirect(reverse("dashboard"))
		
	errors = Review.objects.validate_review(req.POST)
	print(errors)		
	if errors:
		flash_errors(req, errors, "reviewerrors")
		print("error")
		return redirect(reverse("show_book", kwargs={"id":req.POST['book_id']}))
	book = Book.objects.get(id=req.POST['book_id'])	
	review = Review.objects.create_review(req.POST, book)
	
	return redirect(reverse("show_book", kwargs={"id":req.POST['book_id']}))		

def destroy(req, id):
	if not 'user_id' in req.session:
		return redirect(reverse('landing'))
	
	review = Review.objects.filter(id=id)
	if not review.exists():
		return redirect("dashboard")
	
	review = review[0]
	
	
	
	if not req.session['user_id'] == review.user.id:
		return redirect("dashboard")
	
	review.delete()
	return redirect("dashboard")
	