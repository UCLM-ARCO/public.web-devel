# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from eventlog.models import UAV


def index(request):
    context = {'uav_list': UAV.objects.all()}
    return render(request, "index.html", context)
