# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from ..log_reg_app.models import User

# Create your models here.
class TripManager(models.Manager):
    def trip_input_validator(self, form_data):
        errors = []
        if len(form_data['destination']) == 0:
            errors.append("Where are you going?")
        if len(form_data['description']) == 0:
            errors.append("Ohhhh what's it like??")
        if not form_data['travel_start_date']:
            errors.append("When are you leaving??")
        else:
            layout = "%Y-%m-%d"
            date = datetime.strptime(form_data['travel_start_date'], layout)
            current_date = datetime.now()
            if date < current_date:
                errors.append("You have to depart in the future! Physics told me so.")
        if not date:
            errors.append("When are you coming back??")
        else:
            date_return = form_data['travel_end_date']
            arrival_home = datetime.strptime(date_return, layout)
            if arrival_home < date:
                errors.append("Back to the future ehh? you can only come back AFTER you leave.")
        return errors

    def create_trip(self, form_data):
        return self.create(
                destination=form_data['destination'],
                description=form_data['description'],
                travel_start_date=form_data['travel_start_date'],
                travel_end_date=form_data['travel_end_date'],
                creator = form_data['creator']
                )


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    travel_start_date = models.DateTimeField()
    travel_end_date = models.DateTimeField()
    buddy = models.ManyToManyField(User, related_name='buddy')
    creator = models.ForeignKey(User, related_name='creator')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()
