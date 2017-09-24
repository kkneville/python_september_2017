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


    url(r'^works$', views.all_works, name="all_works"),

    url(r'^works/new$', views.new_work, name="new_work"),
    url(r'^works/create$', views.create_work, name="create_work"),

    url(r'^works/(?P<workid>\d+)/show$', views.show_work, name="show_work"),
    url(r'^(?P<id>\d+)/works$', views.show_author_work, name="show_author_work"),

    url(r'^works/(?P<workid>\d+)/edit$', views.worksedit, name="worksedit"),
    url(r'^works/edit_work$', views.edit_work, name="edit_work"),

    url(r'^works/(?P<workid>\d+)/delete$', views.worksdelete, name="worksdelete"),
    url(r'^works/(?P<workid>\d+)/delete_work$', views.delete_work, name="delete_work"),
]
