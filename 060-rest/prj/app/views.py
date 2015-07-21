# -*- coding: utf-8; mode: python -*-

import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from .models import Vehicle
from .forms import VehicleForm


class VehicleList(ListView):
    model = Vehicle
    template_name = 'vehicle-list.html'


class VehicleCreate(CreateView):
    model = Vehicle
    slug_field = 'plate'
    form_class = VehicleForm
    template_name = 'vehicle-edit.html'
    success_url = reverse_lazy('list')


class VehicleUpdate(UpdateView):
    model = Vehicle
    slug_field = 'plate'
    form_class = VehicleForm
    template_name = 'vehicle-edit.html'
    success_url = reverse_lazy('list')


def vehicle_delete(request, plate):
    try:
        Vehicle.objects.get(plate=plate).delete()
    except Vehicle.DoesNotExist:
        pass

    return redirect('list')


def vehicle_gen_file(request, plate):
    destdir = os.path.join(settings.STATIC_ROOT, 'generated')
    if not os.path.isdir(destdir):
        os.makedirs(destdir)

    fpath = os.path.join(destdir, plate)
    with file(fpath, 'w+') as fd:
        fd.write(str(Vehicle.objects.get(plate=plate)))

    context = {'name': os.path.join('generated', plate)}
    return render(request, 'vehicle-file.html', context)


from app.models import Vehicle
from app.serializers import VehicleSerializer
from rest_framework import generics


class VehicleAPIList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
