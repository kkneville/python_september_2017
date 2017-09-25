from __future__ import unicode_literals
from django.db import models
from ..credit_card_app.models import CreditCard, User
from ..service_app.models import Service

class MembershipManager(models.Manager):
    def create_membership(self, form_data, user):
        service = Service.objects.get(id=form_data['service'])
        credit_card = CreditCard.objects.get(id=form_data['credit_card'])
    
        if credit_card.user == user:
            return self.create(
                credit_card = credit_card,
                user = user,
                service = service,
            )
        return False

class Membership(models.Model):
    credit_card = models.ForeignKey(CreditCard, related_name="memberships")
    user = models.ForeignKey(User, related_name="memberships")
    service = models.ForeignKey(Service, related_name="memberships")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MembershipManager()


