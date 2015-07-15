# -*- coding: utf-8; mode: python -*-

import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from .models import Vehicle
from .forms import VehicleForm


class ModelDict(object):
    def __init__(self, model):
        self.model = model

    def get(self, key, default):
        return getattr(self.model, key, default)


def vehicle_list(request):
    context = {'vehicle_list': Vehicle.objects.all()}
    return render(request, "vehicle-list.html", context)


def vehicle_create(request):
    context = {'next': '/vehicle/create/'}
    form = context['form'] = VehicleForm(request.POST or None)

    if not form.is_valid():
        return render(request, 'vehicle-edit.html', context)

    plate = request.POST['plate']
    if Vehicle.objects.filter(plate=plate).exists():
        context['messages'] = "Plate '{}' already exists".format(plate)
        return render(request, 'vehicle-edit.html', context)

    Vehicle(**form.cleaned_data).save()
    return HttpResponseRedirect("/vehicle/list/")


def vehicle_update(request, plate):
    context = {'next': '/vehicle/{}/update/'.format(plate)}

    try:
        vehicle = Vehicle.objects.get(plate=plate)
    except Vehicle.DoesNotExist:
        return HttpResponseRedirect("/vehicle/list/")

    if request.method == 'GET':
        context['form'] = VehicleForm(ModelDict(vehicle))
        return render(request, 'vehicle-edit.html', context)

    form = VehicleForm(request.POST)
    if not form.is_valid():
        context['form'] = form
        return render(request, 'vehicle-edit.html', context)

    for name, value in form.cleaned_data.items():
        if name is "plate":
            continue

        setattr(vehicle, name, value)

    vehicle.save()
    return HttpResponseRedirect("/vehicle/list/")


def vehicle_delete(request, plate):
    try:
        Vehicle.objects.get(plate=plate).delete()
    except Vehicle.DoesNotExist:
        pass

    return HttpResponseRedirect("/vehicle/list/")


def vehicle_gen_file(request, plate):
    destdir = os.path.join(settings.STATIC_ROOT, 'generated')
    if not os.path.isdir(destdir):
        os.makedirs(destdir)

    fpath = os.path.join(destdir, plate)
    with file(fpath, 'w+') as fd:
        fd.write(str(Vehicle.objects.get(plate=plate)))

    context = {'name': os.path.join('generated', plate)}
    return render(request, 'vehicle-file.html', context)
