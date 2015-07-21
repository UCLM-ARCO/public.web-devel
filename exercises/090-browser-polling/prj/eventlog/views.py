# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
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
    model = {'flights': models.Flight}[dataset]
    objects = [m.marshallable() for m in model.objects.all()]
    data = json.dumps(objects)
    return HttpResponse(data)


changes_hash = uuid.uuid4().hex


def get_hash(request):
    return HttpResponse(changes_hash)


@receiver(post_save)
def on_model_save(**kwargs):
    global changes_hash
    changes_hash = uuid.uuid4().hex
