from django.db import models
from django.core.exceptions import ValidationError
import re
import bcrypt
# Create your models here.

class UserManager(models.Manager):
	def validate_registration(self, data):
		errors = []
	
		first_name = data['first_name']
		last_name = data['last_name']
		email = data['email'].lower()
		password = data['password']
		c_password = data['confirm_password']
		
		#first_name
		if len(first_name) < 2:
			errors.append("first name must be greater than 2 characters")
		if not first_name.isalpha():
			errors.append("first name can not contain numbers or special characters")
		
		#last_name
		if len(last_name) < 2:
			errors.append("last name must be greater than 2 characters")
		if not last_name.isalpha():
			errors.append("last name can not contain numbers or special characters")
				
		#email
		result = self.filter(email=email)
		if len(result) != 0:
			errors.append("Email Taken")
		
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
		if len(email) == 0:
			errors.append("Email is required")

		if not EMAIL_REGEX.match(email):
			errors.append("Not a valid email")
	
		#password
		if len(password)<8:
			errors.append("Password must be at least 8 characters.")
		if password != c_password:
			errors.append("Password must match")
		
		return errors

	def validate_login(self, data):
		email = data['email'].lower()
		result = {}
		errors = []
		if len(email) == 0:
			errors.append("Email is required")
	
		if len(data['password'])== 0:
			errors.append("Password is required")
		
		#email
		user = User.objects.filter(email=email).first()
		#if len(user) == 0:
		if user:
			bool = bcrypt.checkpw(data['password'].encode(), user.password.encode())
			print(bool)
			if bool:	
				return {'user':user}
				
		errors.append('email or password does not match')
		return {"errors": errors}
		
	
	def create_user(self, form_data):
		hashpw = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
		return User.objects.create(
			first_name = form_data['first_name'],
			last_name = form_data['last_name'], 
			email = form_data['email'].lower(), 
			password = hashpw,
			)
	
	
class User(models.Model):
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	email = 		models.CharField(max_length=255)
	password = 		models.CharField(max_length=255)
	created_at=		models.DateTimeField(auto_now_add=True)
	updated_at=		models.DateTimeField(auto_now=True)
	objects = UserManager()
	
	def __repr__(self):
		return "|User: {} {} {}|".format(self.first_name, self.last_name, self.email)
