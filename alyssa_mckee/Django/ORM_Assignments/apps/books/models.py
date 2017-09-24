from django.db import models
import re
from django.core.exceptions import ValidationError
# Create your models here.

class AuthorManager(models.Manager):
	def validate_email(self):
		EMAIL_RE = re.compile(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not EMAIL_RE.match(self.email):
			raise ValidationError("email not valid")
	
	def save(self, *args, **kwargs):
		self.validate_email
		super().save(*args, **kwargs)

class Author(models.Model):
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	email = 		models.CharField(max_length=255, unique=True)
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	notes = 		models.TextField(default="")
		
	def __str__(self):
		return "|Author: {} {} {}|".format(self.first_name, self.last_name, self.email)
	
class Book(models.Model):
	name = 			models.CharField(max_length=255)
	desc = 			models.TextField()
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	authors = 		models.ManyToManyField(Author, related_name="books")
	
	
	def __str__(self):
		return "<Book: \"{}\" by {}, {}>".format(self.name, self.authors.all(), self.desc)
	