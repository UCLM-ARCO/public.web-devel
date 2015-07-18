#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

from app.models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
