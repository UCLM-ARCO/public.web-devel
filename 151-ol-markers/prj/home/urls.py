# -*- coding: utf-8; mode: python; -*-

from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'home.views.index'),
]
