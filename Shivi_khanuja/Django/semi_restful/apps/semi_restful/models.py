from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def validate(self,form_data):
        print "validating {}".format(form_data)
        #implement validation here

        return False
    def create_user(self,form_data):
        user = self.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
        )
        return user  
            
            
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= UserManager()

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id , self.first_name, self.last_name, self.email)   