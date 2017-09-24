from django.conf.urls import url 
from . import views 

urlpatterns=[ 
	url(r'^$',views.index, name="landing"),
	url(r'^login$', views.login, name="login"),
	url(r'^register$', views.register, name="register"),
	url(r'^logout$', views.logout, name="logout"),
	url(r'^users/(?P<id>[0-9]+)$', views.show, name="show_user"),
] 
