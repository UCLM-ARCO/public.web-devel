from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request, name):
    html = "Hello <b>{0}</b>!".format(name.capitalize())
    return HttpResponse(html)


def profile(request, name):
    content = """
    <html>
      <head>
        <title>{name}'s Profile</title>
      </head>
      <body>
        <h2>Welcome, {name}. This is your profile!</h2>
        <hr><br><br>

        Name: {name}<br>
        Surname: {surname}<br>
        Age: {age} years
      </body>
    </html>
    """

    context = dict(
        name = name.capitalize(),
        surname = name[::-1].capitalize(),
        age = 20 + len(name),
    )

    html = content.format(**context)
    return HttpResponse(html)
