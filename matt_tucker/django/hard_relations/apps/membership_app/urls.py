from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),
    url(r'^create$', views.create, name="create_membership"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove_membership"),
]