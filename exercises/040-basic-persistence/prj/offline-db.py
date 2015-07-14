#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'prj.settings'

import django
django.setup()

from app.models import Vehicle

Vehicle.objects.all().delete()

v1 = Vehicle(brand='BMW', model='Z3', year=2004, plate='1234 ABC')
v1.save()

v2 = Vehicle(brand='BMW', model='Z4', year=2004, plate='1234 ABC')
v2.save()

print Vehicle.objects.all()
