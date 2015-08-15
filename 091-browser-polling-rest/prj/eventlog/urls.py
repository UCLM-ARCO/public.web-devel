# -*- coding: utf-8; mode: python -*-

from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/uav', views.UAV_viewset)
router.register(r'api/flight', views.Flight_viewset)
router.register(r'api/trackpoint', views.TrackPoint_viewset)

urlpatterns = [
    url(r'^$', views.index),
]

urlpatterns += router.urls
