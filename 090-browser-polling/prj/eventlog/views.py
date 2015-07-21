# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

import models


def index(request):
    return render(request, "eventlog.html")


def insert(request):
    if request.method != "POST":
        return

    # Note: angular sends POST data as JSON, and django does not
    # automatically convert it, do it here
    POST = json.loads(request.body)

    uav = models.UAV.objects.get_or_create(name=POST['uav'])[0]
    uav.save()
    flight = models.Flight(uav=uav, number=POST['flight'], status=2)
    flight.save()

    return HttpResponse("OK")


def get_dataset(request, dataset):
    # If you need to identify AJAX request see: $httpProvider.defaults.headers
    print request.is_ajax()

    model = {'flights': models.Flight}[dataset]
    objects = [m.marshallable() for m in model.objects.all()]
    return JsonResponse(objects, safe=False)
