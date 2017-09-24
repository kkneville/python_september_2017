from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^review$', views.index, name='review_page'),

]
