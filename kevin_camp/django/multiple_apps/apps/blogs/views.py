from django.shortcuts import render, HttpResponse, redirect

def index(request):
	comment = "placeholder to later display all the list of blogs"
	return HttpResponse(comment)

def new(request):
	comment = "placeholder to display a new form to create a new blog"
	return HttpResponse(comment)

def create(request):
	return redirect('/blogs')

def show(request, blog_id):
	comment = "placeholder to display blog {}".format(blog_id)
	return HttpResponse(comment)

def edit(request, blog_id):
	comment = "placeholder to edit blog {}".format(blog_id)
	return HttpResponse(comment)

def delete(request, blog_id):
	comment = "placeholder to delete blog {}".format(blog_id)
	return HttpResponse(comment)
