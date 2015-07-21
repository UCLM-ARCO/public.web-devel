# -*- mode: python; coding: utf-8 -*-

from django.shortcuts import render
from .models import Flight


def index(request):
    context = {'flights': Flight.objects.all()}
    return render(request, "list.html", context)
