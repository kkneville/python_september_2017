from __future__ import unicode_literals
from django.db import models
from ..login_registration_app.models import User

class CreditCardManager(models.Manager):
    def createCreditCard(self, request, form_data):
        return self.create(
            name = form_data['name'],
            number = form_data['number'],
            exp_date = form_data['exp_date'],
            cvv = form_data['cvv'],
            user = User.objects.current_user(request),
        )

class CreditCard(models.Model):
    number = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    exp_date = models.DateField()
    cvv = models.CharField(max_length=4)
    user = models.ForeignKey(User, related_name="credit_cards")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CreditCardManager()
