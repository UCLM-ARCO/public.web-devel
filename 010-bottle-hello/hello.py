#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from bottle import route, run, template


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='', port=8000)
