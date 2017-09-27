from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='landing'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^user_info/(?P<id>\d+)$', views.user_info, name='user_info'),
]
