from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []
        #First name errors
        if len(form_data['first_name']) < 2:
            errors.append("First name is required of at least 2 characters.")
        #Last name
        if len(form_data['last_name']) < 2:
            errors.append("Last name is required of at least 2 characters.")
        #Email
        if len(form_data['email']) == 0:
            errors.append("Email address is required.")
        #Password
        if len(form_data['password']) == 0:
            errors.append("Password is required.")
        #Password confirmation
        if form_data['confirm_PW'] != form_data['confirm_PW']:
            errors.append("Password must match.")

        return errors

    def validate_login(self, form_data):

        #Email
        if len(form_data['email']) == 0:
            errors.append("Email address is required.")
        #Password
        if len(form_data['password']) == 0:
            errors.append("Password is required.")

        user = User.objects.filter(email=form_data['email']).first()

        if user:
            user_password = form_data['password'].encode()
            db_password = user.password.encode()

            if bcrypt.checkpw(user_password, db_password):
                return {'user': user}

        return {'errors': errors}



    def create_user(self, form_data):
        hashedpw  = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())

        return User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = hashedpw,
        )
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        string_output = "id: {} first_name: {} last_name: {} email: {} created_at: {} updated_at: {}"
        return string_output.format (
        self.id,
        self.first_name,
        self.last_name,
        self.email,
        self.created_at,
        self.updated_at,
    )
    objects = UserManager()
