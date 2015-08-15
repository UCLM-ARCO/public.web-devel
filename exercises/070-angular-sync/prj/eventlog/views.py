# -*- mode: python; coding: utf-8 -*-

from django.shortcuts import render
from .models import Flight, UAV


def get_uav(name):
    if name is None or name == "":
        return

    try:
        return UAV.objects.get(name=name)
    except UAV.DoesNotExist:
        pass


def index(request):
    filter_ = {}
    uav = get_uav(request.GET.get('filter'))
    if uav is not None:
        filter_['uav'] = uav

    context = dict(flights=Flight.objects.filter(**filter_))
    return render(request, "list.html", context)
