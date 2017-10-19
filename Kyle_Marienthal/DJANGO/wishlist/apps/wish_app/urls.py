from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^wish_item$', views.wish_item, name='wish_item'),
    url(r'^create$', views.create_item, name='create_item'),
    url(r'^show_wish/(?P<id>\d+)$', views.show_wish, name='show_wish'),
    url(r'^delete_wish/(?P<id>\d+)$', views.delete_wish, name='delete_wish'),
    url(r'^remove_wish/(?P<id>\d+)$', views.remove_wish, name='remove_wish'),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish, name='add_wish'),
    



]
