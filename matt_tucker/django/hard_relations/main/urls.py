from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_registration_app.urls')),
    url(r'^license/', include('apps.driver_license_app.urls')),
    url(r'^credit_card/', include('apps.credit_card_app.urls')),
    url(r'^services/', include('apps.service_app.urls')),
    url(r'^memberships/', include('apps.membership_app.urls')),
    url(r'^friends/', include('apps.friendship_app.urls')),
]
