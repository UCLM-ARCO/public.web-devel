# -*- mode: python; coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return render(request, "register.html")


def valid_form(request):
    password1 = request.POST.get('password')
    password2 = request.POST.get('confirm-password')

    if password1 != password2:
        return HttpResponse("ERROR: Las contraseñas no coinciden!")

    context = request.POST.dict()
    return render(request, "profile.html", context)
