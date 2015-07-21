# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.http import HttpResponse
from geventwebsocket.exceptions import WebSocketError
import json

import models


def index(request):
    return render(request, "eventlog.html")


class PushEvents(object):
    observers = []

    @classmethod
    def on_connect(cls, request):
        ws = request.META["wsgi.websocket"]
        cls.observers.append(ws)

        while not ws.closed:
            try:
                message = ws.receive()
                if message is None:
                    break
            except WebSocketError:
                break

            cls.on_message(message)

        cls.observers.remove(ws)
        return HttpResponse()

    @classmethod
    def on_message(message):
        print "message arrived"

    @classmethod
    def notify(cls, message):
        for o in cls.observers:
            o.send(message)


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

    message = json.dumps(flight.marshallable())
    PushEvents.notify(message)

    return HttpResponse("OK")


def get_dataset(request, dataset):
    model = {'flights': models.Flight}[dataset]
    objects = [m.marshallable() for m in model.objects.all()]
    data = json.dumps(objects)
    return HttpResponse(data)
