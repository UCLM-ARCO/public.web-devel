# -*- coding: utf-8; mode: python -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'api/uav/$', views.UAVAPIList.as_view()),
    url(r'api/uav/(?P<pk>[0-9]+)/$', views.UAVAPIDetail.as_view()),
    url(r'api/flight/$', views.FlightAPIList.as_view()),
    url(r'api/flight/(?P<pk>[0-9]+)/$', views.FlightAPIDetail.as_view()),
    url(r'api/trackpoint/$', views.TrackPointAPIList.as_view()),
    url(r'api/trackpoint/(?P<pk>[0-9]+)/$', views.TrackPointAPIDetail.as_view()),
]
