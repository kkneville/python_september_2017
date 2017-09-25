from django.shortcuts import render, redirect, reverse
from ..login_registration_app.models import User
from .models import Service

def index(request):
    user = User.objects.current_user(request)
    memberships = user.memberships.all()

    # Get a list of all service ids
    service_ids = memberships.values_list('service', flat=True)

    # service_ids = []
    # for membership in memberships:
    #     service_ids.append(membership.service.id)
  

    services = Service.objects.exclude(id__in=service_ids)

    context = {
        "user": user,
        "memberships": memberships,
        "services": services
    }

    return render(request, 'service_app/index.html', context)