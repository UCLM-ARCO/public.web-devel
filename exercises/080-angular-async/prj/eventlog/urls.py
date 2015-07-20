# -*- coding: utf-8; mode: python -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data/(?P<dataset>.+).json', views.get_dataset),
]
