# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.http import HttpResponse
import json
import models


def index(request):
    if request.method == "POST":
        item = models.Item(content=request.POST.get('item'))
        item.save()

    return render(request, "index.html")


def get_items(request):
    objects = [{'content': x.content} for x in models.Item.objects.all()]
    data = json.dumps(objects)
    return HttpResponse(data)
