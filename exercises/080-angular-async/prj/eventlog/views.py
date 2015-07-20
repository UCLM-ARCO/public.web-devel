# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.http import HttpResponse
import json

import models


def index(request):
    return render(request, "event-list.html")


def get_dataset(request, dataset):
    model = {'flights': models.Flight}[dataset]
    objects = [m.marshallable() for m in model.objects.all()]
    data = json.dumps(objects)
    return HttpResponse(data)
