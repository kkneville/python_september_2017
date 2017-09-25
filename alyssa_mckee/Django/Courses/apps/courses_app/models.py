from django.db import models
import re
# Create your models here.
class CourseManager(models.Manager):
	
	def Validate(self, name):
		errors = []
		if len(name)< 5:
			errors.append("name must be more than 5 characters")
		if not re.match(r'[a-zA-Z0-9 -]+', name):
			errors.append("name can only contain letters, numbers and hyphens")
		return errors

class DescriptionManager(models.Manager):
	def Validate(self,desc):
		errors = []
		if len(desc)< 15:
			errors.append("description must be more than 15 characters")
		if not re.match(r'[a-zA-Z0-9 ,.-]+', desc):
			errors.append("name can only contain letters, numbers, ,.-")
		return errors

class Course(models.Model):
	name = 			models.CharField(max_length=255)
	
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	objects = CourseManager()
	
	def __repr__(self):
		return "[Course: name = {} {} {}]\n".format(self.name, self.desc, self.created_at)
	
class Description(models.Model):
	content = 		models.TextField()
	course = 		models.OneToOneField(Course, related_name="desc")
	
	created_at = 	models.DateTimeField(auto_now_add=True)
	updated_at = 	models.DateTimeField(auto_now=True)
	objects = DescriptionManager()
	def __repr__(self):
		return "<Description: {}>".format(self.context)
	
def insert_Course_and_Description(form_data):
	course = Course.objects.create(name=form_data['name'])
	Description.objects.create(content=form_data['desc'], course=course)
	print('success ^_^')
	
def delete_Course_and_Description(id):
	course = Course.objects.filter(id=id)
	if course:
		course[0].desc.delete()
		course.delete()
	print('success ^_^')