from django.conf.urls import url 
from . import views 

urlpatterns=[ 
	url(r'^$',					  	views.index,	name="all_users"),
	url(r'^new', 				  	views.new, 	name="new"),
	url(r'^(?P<id>[0-9]+)/edit$', 	views.edit,	name="edit"),
	url(r'^(?P<id>[0-9]+)$',	  	views.show,	name="show_user" ),
	url(r'^create$', 			  	views.create, name="create_user"),
	url(r'^(?P<id>[0-9]+)/update$',	views.update, name="update_user"),
	url(r'^(?P<id>[0-9]+)/delete$',	views.destroy, name="delete"),
] 
