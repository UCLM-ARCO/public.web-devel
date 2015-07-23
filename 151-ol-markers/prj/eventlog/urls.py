# -*- coding: utf-8; mode: python -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^insert/', views.insert),
    url(r'^data/(?P<dataset>.+).json', views.get_dataset),
    url(r'^uav/(?P<name>.+)', views.get_uav_profile),

    # websockets
    url(r'^ws', views.PushEvents.on_connect),
]
