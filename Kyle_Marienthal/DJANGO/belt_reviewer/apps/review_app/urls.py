from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='review_page'),
    url(r'^create_review$', views.create_review, name='create_review'),

]
