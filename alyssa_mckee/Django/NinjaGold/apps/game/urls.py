from django.conf.urls import url 
from . import views 

urlpatterns=[ 
	url(r'^game$',views.index),
	url(r'^game/process_money$', views.process),
	url(r'^new$', views.new)
] 
