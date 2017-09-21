from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.
class Deleted_User(models.Model):
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	email = 		models.CharField(max_length=255)
	deleted_at=		models.DateTimeField(auto_now_add=True)
	
	def __repr__(self):
		return "|Deleted User: {} {} {}|".format(self.first_name, self.last_name, self.email)

class UserManager(models.Manager):
	def validate(self, form_data):
		errors = {}
		
		first_name = form_data['first_name']
		last_name = form_data['last_name']
		email = form_data['email'].lower()
		
		#first_name
		if len(first_name) < 2:
			errors['first_name'] = ["first name must be greater than 2 characters"]
		if not first_name.isalpha():
			if 'first_name' not in errors:
				errors['first_name'] = []
			errors['first_name'].append("First name can not contain special characters")
	
		#last_name
		if len(last_name) < 2:
			errors['last_name'] = ["last name must be greater than 2 characters"]
		if not last_name.isalpha():
			if 'last_name' not in errors:
				errors['last_name'] = []
			errors['last_name'].append("last name can not contain numbers or special characters")
		
		#email
		result = self.filter(email = email)
		if len(result) != 0:
			errors['email'] = ["Email Taken"]
	
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
		if len(email) == 0:
			if 'email' not in errors:
				errors['email'] = []
			errors['email'].append("Email is required")
		if not EMAIL_REGEX.match(email):
			if 'email' not in errors:
				errors['email'] = []
			errors['email'].append("Not a valid email")
			
		return errors


	def create_user(self, form_data):
		first_name = form_data['first_name']
		last_name = form_data['last_name']
		email = form_data['email']
		user = self.create(first_name = form_data['first_name'], last_name = form_data['last_name'], email = form_data['email'])
		return user
	
	def edit_user(self, form_data):
		user = self.get(id=form_data['id'])
		
		user.first_name = form_data['first_name']
		user.last_name = form_data['last_name']
		user.email = form_data['email']
		user.save()
		return user
	
	def destroy(self, id):
		user = self.get(id=id)
		deleted = Deleted_User.objects.create(first_name = user.first_name, last_name=user.last_name, email=user.email)
		user.delete()
		return deleted
	
	
class User(models.Model):
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	email = 		models.CharField(max_length=255)
	created_at=		models.DateTimeField(auto_now_add=True)
	updated_at=		models.DateTimeField(auto_now=True)
	objects = UserManager()
	
	def __repr__(self):
		return "|User: {} {} {}|".format(self.first_name, self.last_name, self.email)
		
class Deleted_Users(models.Model):
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	email = 		models.CharField(max_length=255)
	deleted_at=		models.DateTimeField(auto_now_add=True)
	
	def __repr__(self):
		return "|Deleted User: {} {} {}|".format(self.first_name, self.last_name, self.email)