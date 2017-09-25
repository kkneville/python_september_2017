from __future__ import unicode_literals
from django.db import models
from ..login.models import User
from ..book_app.models import Book

class ReviewManager(models.Manager):
    pass

class Review(models.Model):
    content= models.TextField()
    rating= models.IntegerField()
    book=models.ForeignKey(Book,related_name="reviews")
    User=models.ForeignKey(User,related_name="reviews")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects=ReviewManager()