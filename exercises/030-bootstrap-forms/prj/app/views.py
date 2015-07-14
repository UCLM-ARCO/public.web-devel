# -*- mode: python; coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse


class UserStorage(object):
    users = {}

    @classmethod
    def add(cls, fields):
        name = fields['username']
        cls.users[name] = fields

    @classmethod
    def get(cls, name):
        return cls.users.get(name, None)


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = UserStorage.get(username)

    if user is None or password != user['password']:
        return render(request, "login.html", {'error': "Invalid user or password!"})

    return redirect("/profile/{}/".format(username))


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    password1 = request.POST.get('password')
    password2 = request.POST.get('confirm-password')

    if password1 != password2:
        return HttpResponse("ERROR: Las contraseñas no coinciden!")

    UserStorage.add(dict(request.POST.items()))
    return redirect("/")


def profile(request, name):
    user = UserStorage.get(name)
    if user is None:
        return redirect("/")

    return render(request, "profile.html", user)
