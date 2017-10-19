from django.conf.urls import url 
from . import views 

urlpatterns=[  
	url(r'^create$', views.create, name="create_review"),
	url(r'^destroy/(?P<id>[0-9]+)$', views.destroy, name="destroy_review")
] 
