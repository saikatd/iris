from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.campaigns, name='campaigns'),
    url(r'^campaign/(?P<campaign_id>[0-9]+)/$', views.eyes_captured, name='eyes_captured'),
    url(r'^driver/(?P<driver_id>[0-9]+)/$', views.driver_eyes_captured, name='driver_eyes_captured'),
]
