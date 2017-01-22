from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^eyes/$', views.eyes_captured, name='eyes_captured'),
    url(r'^eyes/(?P<driver_id>[0-9]+)/$', views.driver_eyes_captured, name='driver_eyes_captured'),
]
