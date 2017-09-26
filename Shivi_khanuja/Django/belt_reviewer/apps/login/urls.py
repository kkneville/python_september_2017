from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$',views.index, name="landing"),
    url(r'^register$',views.register, name="register"),
    url(r'^login$',views.login, name="login"),
    url(r'^logout$',views.logout, name="logout"),
    # url(r'^success',views.success,name="dashboard")
    url(r'^show/(?P<id>\d+)$',views.show,name="show_user"),
]

# Named Routes
# HTML => {% url 'show_user' id=user.id %}
# views.py => reverse('show_user', kwargs={'id': user.id})