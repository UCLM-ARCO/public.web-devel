"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from app import views


urlpatterns = [
    url(r'api/$',
        views.VehicleAPIList.as_view()),
    url(r'api/(?P<pk>[0-9]+)/$',
        views.VehicleAPIDetail.as_view()),

    url(r'list/$',
        views.VehicleList.as_view(), name='list'),
    url(r'create/$',
        views.VehicleCreate.as_view(), name='create'),
    url(r'(?P<slug>.+)/update/',
        views.VehicleUpdate.as_view(), name='update'),
    url(r'(?P<plate>.+)/delete/',
        'app.views.vehicle_delete', name='delete'),
    url(r'(?P<plate>.+)/gen-file/',
        'app.views.vehicle_gen_file'),
]
