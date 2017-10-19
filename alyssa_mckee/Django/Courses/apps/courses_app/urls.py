from django.conf.urls import url 
from . import views 

urlpatterns=[ 
	url(r'^$',views.index, name="landing"), 
	url(r'^process$', views.process, name="new_course"),
	url(r'^destroy/(?P<id>[0-9]+)$', views.destroy, name="destroy_course"),
	url(r'^process_destroy/(?P<id>[0-9]+)$', views.process_destroy, name="process_destroy")
] 
