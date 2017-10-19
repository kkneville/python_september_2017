from django.db import models
from django.core.exceptions import ValidationError
import re
import bcrypt
# Create your models here.

class UserManager(models.Manager):
	def validate_registration(self, data):
		errors = []
	
		name = data['name']
		alias = data['alias']
		email = data['email'].lower()
		password = data['password']
		c_password = data['confirm_password']
		
		#name
		if len(name) < 2:
			errors.append("name must be greater than 2 characters")
		if not name.isalpha():
			errors.append("name can not contain numbers or special characters")
		
		#alias
		if len(alias) < 2:
			errors.append("alias must be greater than 2 characters")
		if not alias.isalpha():
			errors.append("alias can not contain numbers or special characters")
				
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
			name = form_data['name'],
			alias = form_data['alias'], 
			email = form_data['email'].lower(), 
			password = hashpw,
			)
	
	def get_user(self, user_id):
		return User.objects.filter(id=user_id)
class User(models.Model):
	name = 			models.CharField(max_length=255)
	alias = 		models.CharField(max_length=255)
	email = 		models.CharField(max_length=255)
	password = 		models.CharField(max_length=255)
	
	created_at=		models.DateTimeField(auto_now_add=True)
	updated_at=		models.DateTimeField(auto_now=True)
	
	objects = 		UserManager()
	
	def __repr__(self):
		return "|User: {} {} {}|".format(self.name, self.alias, self.email)
