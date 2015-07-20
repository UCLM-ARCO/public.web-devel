# -*- coding: utf-8; mode: python -*-

from django.db import models


class UAV(models.Model):
    name = models.CharField(max_length=30)

    def marshallable(self):
        return {'name': self.name}


class Flight(models.Model):
    STATUS_OK = 0
    STATUS_ISSUES = 1
    STATUS_FAILURE = 2

    uav = models.ForeignKey(UAV)
    number = models.CharField(max_length=10)
    status = models.SmallIntegerField(
        choices=((STATUS_OK, "Flight OK"),
                 (STATUS_ISSUES, "Flight has Issues"),
                 (STATUS_FAILURE, "Flight Failure"))
    )

    def __unicode__(self):
        return 'Flight {} (uav:{})'.format(self.number, self.uav)

    def marshallable(self):
        return {
            'uav': self.uav.marshallable(),
            'number': self.number,
            'status': self.status,
        }


class TrackPoint(models.Model):
    flight = models.ForeignKey(Flight)
    timestamp = models.DateTimeField()

    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()

    def marshallable(self):
        return {
            'flight': self.flight.marshallable(),
            'timestamp': self.timestamp,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
        }
