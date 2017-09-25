from django.shortcuts import render, redirect, reverse
from .models import Course, Description, insert_Course_and_Description, delete_Course_and_Description
from django.contrib import messages
from time import strftime
# Create your views here.

def flash_messages(errors, req):
	for error in errors:
		messages.add_message(req, messages.ERROR, error)

def index(req): 
	context = {"courses":[]}
	courses = Course.objects.all()
	if courses:
		for course in courses:
			time = course.created_at
			context['courses'].append({ "name":course.name, "desc":course.desc.content, "created_at":course.created_at, "id":course.id})
	
	return render(req,"courses_app/index.html", context)
	
def process(req):
	course_errors = Course.objects.Validate(req.POST['name'])
	description_errors = Description.objects.Validate(req.POST['desc'])
	
	if course_errors:
		flash_messages(course_errors, req)
	if description_errors:
		flash_messages(description_errors, req)
	
	if not course_errors and not description_errors:
		#input to database
		insert_Course_and_Description(req.POST)
	
	return redirect(reverse("landing"))

def destroy(req, id):
	context = {"id":id}
	course = Course.objects.filter(id=id)
	if not course:
		return redirect(reverse("landing"))
	context["name"] = course[0].name
	context["desc"] = course[0].desc.content
	
	return render(req,"courses_app/confirm_destroy.html", context)
	
def process_destroy(req, id):
	if req.method == "POST":
		delete_Course_and_Description(id)
	return redirect(reverse("landing"))