# -*- coding: utf-8; mode: python -*-

import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import View

from .models import Vehicle
from .forms import VehicleForm


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


class VehicleUpdate(View):
    http_method_names = ['get', 'post']

    def get_context(self, plate, **kargs):
        context = {'next': reverse('update', args=(plate,))}
        context.update(kargs)
        return context

    def get_vehicle(self, plate):
        try:
            return Vehicle.objects.get(plate=plate)
        except Vehicle.DoesNotExist:
            return HttpResponseRedirect("/vehicle/list/")

    def get(self, request, plate):
        context = self.get_context(
            plate, form=VehicleForm(instance=self.get_vehicle(plate)))
        return render(request, 'vehicle-edit.html', context)

    def post(self, request, plate):
        form = VehicleForm(request.POST, instance=self.get_vehicle(plate))

        if not form.is_valid():
            context = self.get_context(plate, form=form)
            return render(request, 'vehicle-edit.html', context)

        form.save()
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
