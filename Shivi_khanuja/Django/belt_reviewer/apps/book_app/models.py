from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
    pass


class Book(models.Model):
    title= models.CharField(max_length=150)
    author= models.CharField(max_length=150)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects=BookManager()
