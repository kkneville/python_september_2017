from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="all_friends"),
    url(r'^add/(?P<id>\d+)$', views.add, name="add_friend"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove_friend"),
]