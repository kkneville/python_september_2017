from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.all, name="all"),
    url(r'^new$', views.new, name="new_user"),
    url(r'^create$', views.create, name="create"),
    url(r'^(?P<id>\d+)$', views.show, name="show"),
    url(r'^(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r'^(?P<id>\d+)/edit_user$', views.edit_user, name="edit_user"),
    url(r'^(?P<id>\d+)/delete$', views.delete, name="delete"),
    url(r'^(?P<id>\d+)/delete_user$', views.delete_user, name="delete_user"),
]
