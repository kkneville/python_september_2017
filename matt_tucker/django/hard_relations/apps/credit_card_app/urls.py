from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="all_credit_cards"),
    url(r'^add$', views.add, name="add_credit_card"),
    url(r'^create$', views.create, name="create_credit_card"),
]