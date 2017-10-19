from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="all_users"),
    url(r'^new$', views.new, name="new_user"),
    url(r'^create$', views.create, name="create_user"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show_user"),
]