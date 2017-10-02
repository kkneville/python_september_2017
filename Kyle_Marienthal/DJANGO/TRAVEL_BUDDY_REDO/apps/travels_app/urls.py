from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^add_trip$', views.add_trip, name='add_trip'),
    url(r'^create_trip$', views.create_trip, name='create_trip'),
    url(r'^destination/(?P<id>\d+)$', views.destination, name = "destination")

]
