from django.conf.urls import url 
from . import views 

urlpatterns=[ 
	url(r'^$',views.index, name="dashboard"), 
	url(r'^(?P<id>[0-9]+)$', views.show, name="show_book"),
	url(r'^add$', views.add, name="add_book"),
	url(r'^create$', views.create, name="create"),
] 
