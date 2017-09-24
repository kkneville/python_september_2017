from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$',views.index, name="users"),
    url(r'^register/$',views.register, name="register"),
    url(r'^login/$',views.login, name="login"),
]
