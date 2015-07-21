# -*- coding: utf-8; mode: python -*-

from django.db import models


class UAV(models.Model):
    name = models.CharField(max_length=30)


class Flight(models.Model):
    number = models.CharField(max_length=10)
    uav = models.ForeignKey(UAV)


class TrackPoint(models.Model):
    flight = models.ForeignKey(Flight)
    timestamp = models.DateTimeField()

    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
