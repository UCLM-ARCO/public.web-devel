# -*- coding: utf-8; mode: python; -*-

from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'maps.views.index'),
    url(r'^tile.json', 'maps.views.tilejson'),
    url(r'^points/', 'maps.views.get_flight_points'),
]
