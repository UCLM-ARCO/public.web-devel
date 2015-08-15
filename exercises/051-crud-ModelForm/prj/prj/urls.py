"""prj URL Configuration

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
from django.views.generic import RedirectView

from app.views import VehicleUpdate

urlpatterns = [
    url(r'^vehicle/list/$', 'app.views.vehicle_list'),
    url(r'^vehicle/create/$', 'app.views.vehicle_create'),
    url(r'^vehicle/(?P<plate>.+)/update/', VehicleUpdate.as_view(), name='update'),
    url(r'^vehicle/(?P<plate>.+)/delete/', 'app.views.vehicle_delete'),

    url(r'^vehicle/(?P<plate>.+)/gen-file/', 'app.views.vehicle_gen_file'),

    url(r'^brand/create/$',
        'app.views.brand_create'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url="/vehicle/list/", permanent=False)),
]
