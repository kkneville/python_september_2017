# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..book_app.models import Book
from ..log_reg_app.models import User


# Create your models here.
class ReviewManager(models.Manager):
    def validate(self, form_data):
        errors = []
        #content
        if len(form_data['content']) == 0:
            errors.append('review content is required.')
        return errors

    def create_review(self, form_data, book, user):
        return self.create(
            content = form_data['content'],
            rating = form_data['rating'],
            book = book,
            user = user
            )



class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name = 'reviews')
    user = models.ForeignKey(User, related_name = 'reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()
