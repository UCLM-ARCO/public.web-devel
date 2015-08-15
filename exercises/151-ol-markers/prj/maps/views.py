# -*- coding: utf-8; mode: python; -*-

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from eventlog import models


@login_required
def index(request):
    return render(request, 'maps.html')


@login_required
def tilejson(request):
    retval = {
        "tilejson": "2.1.0",
        "attribution": "The Middle Earth",
        "tiles": [
            "/static/maps/tiles/{z}/{x}/{y}.jpg"
        ],
        "minzoom": 0,
        "maxzoom": 6,
    }

    # OS3.TileJSON usually requires a JSONP response
    data = json.dumps(retval)
    callback = request.GET.get('callback', None)
    if callback:
        data = "{}({})".format(callback, data)
        return HttpResponse(data, "text/javascript")

    return HttpResponse(data, "application/json")


@login_required
def get_flight_points(request):
    data = {}
    flights = models.Flight.objects.all()
    for f in flights:
        points = models.TrackPoint.objects.filter(flight=f)
        points = [p.marshallable() for p in points]
        data[f.number] = points

    data = json.dumps(data)
    return HttpResponse(data, "application/json")
