from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
from django.db import models
import random, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, formdata):
        errors = []
        if (len(formdata['firstname']) < 2) or (not formdata['firstname'].isalpha()):
            errors.append("Invalid first name.")
        if (len(formdata['lastname']) < 2) or (not formdata['lastname'].isalpha()):
            errors.append("Invalid last name.")
        if not EMAIL_REGEX.match(formdata['email']):
            errors.append("Invalid email address.")
        return errors


    def create_user(self, formdata):
        user = self.create (
            firstname = formdata['firstname'],
            lastname = formdata['lastname'],
            email = formdata['email'],
        )
        return user

    def edit(self, formdata):
        user = User.objects.get(id=formdata['id'])
        user.firstname = formdata['firstname']
        user.lastname = formdata['lastname']
        user.email = formdata['email']
        user.save()
        return user

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class WorkManager(models.Manager):
    def validate(self, formdata):
        errors = []
        if len(formdata['title']) < 1 :
            errors.append("New works must have a title.")
        return errors

    def create_work(self, formdata):
        work = self.create (
            title = formdata['title'],
            year = formdata['year'],
            author = User.objects.get(id=formdata['author']),
            desc = formdata['desc'],
        )
        return work

    def edit(self, formdata):
        work = Work.objects.get(id=formdata['workid'])
        work.title = formdata['title']
        work.year = formdata['year']
        work.save()
        return work


class Work(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    desc = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name="works")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = WorkManager()
