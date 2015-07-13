#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/profile/<name>')
def profile(name):
    content = """
    <html>
      <head>
        <title>{{name}}'s Profile</title>
      </head>
      <body>
        <h2>Welcome, {{name}}. This is your profile!</h2>
        <hr><br><br>

        Name: {{name}}<br>
        Surname: {{surname}}<br>
        Age: {{age}} years
      </body>
    </html>
    """

    context = dict(
        name = name.capitalize(),
        surname = name[::-1].capitalize(),
        age = 20 + len(name),
    )

    return template(content, **context)


print("Visit http://localhost:8080/profile/thomas")
run(host='localhost', port=8000)
