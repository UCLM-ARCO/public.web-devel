# -*- coding: utf-8; mode: python; -*-

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'maps.html')


@login_required
def tilejson(request):
    retval = {
        "tilejson": "2.1.0",
        "attribution": "Arco Research Group (C) 2015",
        "tiles": [
            "/static/maps/tiles/{z}/{x}/{y}.jpg"
        ],
        "minzoom": 0,
        "maxzoom": 7,
    }

    # OS3.TileJSON usually requires a JSONP response
    data = json.dumps(retval)
    callback = request.GET.get('callback', None)
    print "callback is", callback
    if callback:
        data = "{}({})".format(callback, data)
        return HttpResponse(data, "text/javascript")

    return HttpResponse(data, "application/json")
