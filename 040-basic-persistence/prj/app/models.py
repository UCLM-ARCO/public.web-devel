# -*- coding: utf-8; mode: python -*-

from django.db import models


class Vehicle(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    plate = models.CharField(max_length=12, unique=True, primary_key=True)
    year = models.IntegerField()
