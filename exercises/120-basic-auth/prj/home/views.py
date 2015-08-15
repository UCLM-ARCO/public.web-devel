# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render, redirect
from eventlog.models import UAV
import forms


def index(request):
    context = {'uav_list': UAV.objects.all()}
    return render(request, "index.html", context)


def register_user(request):
    if request.method == "GET":
        form = forms.UserCreationForm()

    else:
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/register/done/")

    return render(request, "registration/register.html", {'form': form})


def register_user_done(request):
    return render(request, "registration/register_done.html")
