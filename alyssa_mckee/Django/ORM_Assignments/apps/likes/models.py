from django.db import models

# Create your models here.
class User(models.Model):
	first_name= 	models.CharField(max_length=255)
	last_name= 		models.CharField(max_length=255)
	email=			models.CharField(max_length=255)
	created_at= 	models.DateTimeField(auto_now_add=True)
	updated_at= 	models.DateTimeField(auto_now=True)
	
	def __repr__(self):
		return "|User: {} {} {} |\n".format(self.first_name, self.last_name, self.email)
	
class Book(models.Model):
	name = 			models.CharField(max_length=255)
	desc = 			models.TextField()
	created_at= 	models.DateTimeField(auto_now_add=True)
	updated_at=		models.DateTimeField(auto_now=True)
	uploader =		models.ForeignKey(User, related_name="uploaded_books")
	
	def __repr__(self):
		return '<Book: "{}" {}>\n'.format(self.name, self.desc)
	
class Like(models.Model):
	user = 		models.ForeignKey(User, related_name="liked_books")
	book = 		models.ForeignKey(Book, related_name="liked_users")
	def __repr__(self):
		return '<3 Like: "{}" liked by {} <3\n'.format(self.book.name, self.user.first_name)
