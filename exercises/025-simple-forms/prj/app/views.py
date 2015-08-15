from django.shortcuts import render, redirect
from django.http import HttpResponse


username = None


def index(request):
    return render(request, "simple-form.html")


def save_form(request):
    global username
    username = request.POST['name']
    print "Login USER: " + username

    return redirect("/show/")


def show_profile(request):
    if username is None:
        return redirect("/")

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
        name = username.capitalize(),
        surname = username[::-1].capitalize(),
        age = 20 + len(username),
    )

    html = content.format(**context)
    return HttpResponse(html)
