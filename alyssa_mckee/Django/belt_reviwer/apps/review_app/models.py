from django.db import models
from ..book_app.models import Book
from ..login_registration.models import User
# Create your models here.
class ReviewManager(models.Manager):
	def validate_review(self, data):
		errors = []
		if len(data['content']) == 0:
			errors.append("review can not be empty")
		return errors

	def create_review(self, data, book):
		print(data)
		return Review.objects.create(
			content=data['content'],
			rating=int(data['rating']),
			book=book,
			user=User.objects.get(id=data['user_id'])
		)
	
	
class Review(models.Model):
	content = 		models.TextField()
	rating = 		models.IntegerField()
	
	book = 			models.ForeignKey(Book, related_name="reviews")
	user = 			models.ForeignKey(User, related_name="reviews")
	
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	
	objects = ReviewManager()
	
	def __str__(self):
		return "{} {} {} {}".format(self.user, self.book, self.content, self.rating)