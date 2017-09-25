from django.shortcuts import render, redirect, reverse
from .models import License


def add(request):
    return render(request, 'driver_license_app/add.html')

def create(request):
    if request.method == "POST":
        license = License.objects.create_license(request, request.POST)

        return redirect(reverse('show_license', kwargs={'id': license.id}))

    return redirect(reverse('add_license'))

def show(request, id):
    license = License.objects.filter(id=id).first()

    if license:
        return render(request, 'driver_license_app/show.html', {'license': license})

    return render(request, 'driver_license_app/hell.html', {'times': range(0, 100)})

