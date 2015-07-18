# -*- coding: utf-8; mode: python -*-

from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name


class Vehicle(models.Model):
    brand = models.ForeignKey(Brand)
    model = models.CharField(max_length=30)
    plate = models.CharField(max_length=12, unique=True)
    year = models.IntegerField()

    def __unicode__(self):
        return "{}; {} {}".format(self.plate, self.brand, self.model)
