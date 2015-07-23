# -*- coding: utf-8; mode: python; -*-

from django.conf.urls import url

urlpatterns = [
    url('list/', 'app.views.get_items'),
    url('', 'app.views.index'),
]
