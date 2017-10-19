# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from ..log_reg_app.models import User
# Create your models here.
class TripManager(models.Manager):
    def validate_travel_dates(self, form_data):
        errors = []
        if len(form_data['destination']) == 0:
            errors.append("Where are you going?")
        if len(form_data['description']) == 0:
            errors.append("Ohhhh what's it like??")
        if len(form_data['travel_date_from']) == 0:
            errors.append("When are you leaving??")
        else:
            layout = "%Y-%m-%d"
            # date = when they leave
            date = datetime.strptime(form_data['travel_date_from'], layout)
            current_date = datetime.now()
            if date < current_date:
                errors.append("You have to depart in the future! Physics told me so.")
        if len(date) == 0:
            errors.append("When are you coming back??")
        else:
            date_return = form_data['travel_date_to']
            arrival_home = datetime.strptime(date_return, layout)
            if arrival_home < date:
                errors.append("Back to the future ehh? you can only come back AFTER you leave.")
        return errors

    def create_trip(self, form_data, user):
        print '*****youre in the create_trip method*****'
        return self.create(
            destination = form_data['destination'],
            description = form_data['description'],
            travel_date_from = form_data['travel_date_from'],
            travel_date_to = form_data['travel_date_to'],
            planner = user
        )



class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    planner = models.ForeignKey(User, related_name = 'trip_planner')
    buddy = models.ManyToManyField(User, related_name = 'travel_buddies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
