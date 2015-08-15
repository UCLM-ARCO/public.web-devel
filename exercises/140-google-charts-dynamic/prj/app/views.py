# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.http import HttpResponse
from geventwebsocket.exceptions import WebSocketError
from threading import Thread
import time
import json
import random


def index(request):
    return render(request, "index.html")


class PointGenerator(Thread):
    def __init__(self):
        super(PointGenerator, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            time.sleep(float(random.randint(0, 10)) / 10)
            event = {'x': random.randrange(0, 100), 'y': random.randrange(0, 100)}
            PushEvents.notify(json.dumps(event))


PointGenerator().start()


class PushEvents(object):
    observers = []

    @classmethod
    def on_connect(cls, request):
        ws = request.META["wsgi.websocket"]
        cls.observers.append(ws)

        while not ws.closed:
            try:
                if ws.receive() is None:
                    break
            except WebSocketError:
                break

        cls.observers.remove(ws)
        return HttpResponse()

    @classmethod
    def notify(cls, message):
        for o in cls.observers:
            o.send(message)
