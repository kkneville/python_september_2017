from __future__ import unicode_literals
from django.db import models
from ..login_registration_app.models import User

# Create your models here.
class LicenseManager(models.Manager):
    def create_license(self, request, form_data):
        return self.create(
            number = request.POST['number'],
            name = request.POST['name'],
            exp_date = request.POST['exp_date'],
            user = User.objects.current_user(request)
        )

class License(models.Model):
    number = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    exp_date = models.DateField()
    user = models.OneToOneField(User, related_name="license")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LicenseManager()
