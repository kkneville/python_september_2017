from django.conf.urls import url
from . import views
import random


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process_money),
        
]
