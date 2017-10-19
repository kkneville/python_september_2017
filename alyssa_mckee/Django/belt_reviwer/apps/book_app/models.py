from django.db import models
import re

# Create your models here.
class AuthorManager(models.Manager):
	def validate_author(self, data):
		errors = []
		#new_author takes presidense over existing
		
		#if no new specified and no author chosen:
		print(not data['new_author'] or not data['existing_author'])
		if data['new_author']=="" and data['existing_author']=="":
			errors.append("Author can not be empty")
		
		#if new author is not empty and is not alpha (with spaces between)
		if data['new_author'] != "" and not re.match(r'^[a-zA-Z]+([a-zA-Z ]?[a-zA-Z]+)*$',data['new_author']):
			errors.append("Author name is not valid. Letters and spaces between words only.")
		
		return errors
		
	
	def get_author(self, id):
		return Author.objects.filter(name=name)


class Author(models.Model):
	name = 		models.CharField(max_length=255)
	objects = AuthorManager()
	
	def __str__(self):
		return "{}".format(self.name)

class BookManager(models.Manager):
	
	def validate_book(self, data):
		#name
		errors = []
		if len(data['title']) <1:
			errors.append("Title can not be empty")
		return errors
	
	def create_book(self, data):
		result = {}
		
		#if no new author specified, use the existing to create book
		if data['new_author']=="":
			author = Author.objects.get(id= int(data['existing_author']) )
		else:
			author = Author.objects.create(name = data['new_author'])
		
		book = Book.objects.create(title=data['title'], author=author)
		
		return book


class Book(models.Model):
	title = 		models.CharField(max_length=255)
	
	author = 		models.ForeignKey(Author, related_name="books")
	
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	
	objects = BookManager()
	
	def __str__(self):
		return '"{}" {}'.format(self.title, self.author)
