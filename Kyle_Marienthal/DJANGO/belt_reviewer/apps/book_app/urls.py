from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book, name='dashboard'),
    url(r'^info$', views.book_info, name='book_info'),
    url(r'^add$', views.add_book, name='add_book'),
    url(r'^create$', views.create_book, name='create_book'),
    url(r'^show/(?P<id>\d+)$', views.show_book, name='show_book'),

]
