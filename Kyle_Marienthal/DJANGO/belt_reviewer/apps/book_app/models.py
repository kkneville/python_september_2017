from django.db import models
from ..log_reg_app.models import User

class BookManager(models.Manager):
    def validate(self, form_data):
        errors = []
        # title
        if len(form_data['title']) == 0:
            errors.append('title is required.')
        # author
        if len(form_data['author']) == 0:
            errors.append('author is required')

        return errors

    def create_book(self, form_data):
        return self.create(
            title=form_data['title'],
            author=form_data['author']
        )

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
