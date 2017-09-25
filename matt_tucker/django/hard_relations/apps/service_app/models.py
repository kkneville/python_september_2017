from __future__ import unicode_literals
from django.db import models

class ServiceManager(models.Manager):
    pass

class Service(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ServiceManager()