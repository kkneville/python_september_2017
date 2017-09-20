from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.
class User(models.Model):
	first_name = 	models.CharField(max_length=255)
	last_name = 	models.CharField(max_length=255)
	email_address = models.CharField(max_length=255, unique=True)
	age = 			models.IntegerField()
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return "|User: {} {} {} {}|".format(self.first_name, self.last_name, self.email_address, self.age)
	
	def save(self, *args, **kwargs):
		if len(self.first_name) == 0:
			raise ValidationError('first_name can not be empty!')
		
		if not self.first_name.isalpha():
			raise ValidationError("first name can not contain numbers or special characters")
		if len(self.last_name) == 0:
			raise ValidationError('last_name can not be empty!')
		
		if not self.first_name.isalpha():
			raise ValidationError("first name can not contain numbers or special characters")
		if self.age < 0:
			raise ValidationError("age can not be negative")
		
		EMAIL_RE = re.compile(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not EMAIL_RE.match(self.email_address):
			raise ValidationError("email not valid")
			
		super().save(*args, **kwargs)