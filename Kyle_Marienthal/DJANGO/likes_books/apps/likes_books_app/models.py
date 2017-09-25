# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '"id:"{} - {} - {}'.format(self.id, self.name, self.email)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likes = models.ManyToManyField(User, related_name = 'likes')
    uploader = models.ForeignKey(User, related_name = 'uploader')

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.id, self.name, self.desc, self.uploader)

# class Like(models.Model):
#     liked_books = models.ForeignKey(Book, related_name = 'liked_books')
#     liked_users = models.ForeignKey(User, related_name = 'liked_users')
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
