from django.conf.urls import url, include
from django.contrib import admin
import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^words$',views.create),
    url(r'^clear$',views.clear),

]