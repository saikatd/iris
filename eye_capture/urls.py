from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^first/', views.eye_balls_captured, name='eye_balls_captured')
]
