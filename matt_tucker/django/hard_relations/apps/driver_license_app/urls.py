from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add, name="dashboard"),
    url(r'^add$', views.add, name="add_license"),
    url(r'^create$', views.create, name="create_license"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show_license"),
]