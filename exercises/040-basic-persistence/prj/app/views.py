# -*- coding: utf-8; mode: python -*-

from django.shortcuts import render

from .forms import VehicleForm
from .models import Vehicle


def vehicle_create(request):
    context = {}

    if request.method == "POST":
        form = VehicleForm(request.POST)

        if form.is_valid():
            save_vehicle(form.cleaned_data)
            context['status'] = "added"
            form = VehicleForm()
    else:
        form = VehicleForm()

    context['form'] = form
    return render(request, 'vehicle-edit.html', context)


def save_vehicle(fields):
    v = Vehicle(**fields)
    v.save()


def vehicle_list(request):
    context = {'vehicles': Vehicle.objects.all()}
    return render(request, 'vehicle-list.html', context)
