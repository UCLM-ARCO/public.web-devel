from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "simple-form.html")


def print_form(request):
    name = request.POST['name']
    response = "OK <!-- name: {} -->".format(name)

    print "\nLogin USER: {}\n".format(name)
    return HttpResponse(response)
