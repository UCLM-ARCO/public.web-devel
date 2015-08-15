# -*- coding: utf-8; mode: python -*-

from rest_framework import serializers
from eventlog import models


class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UAV


class FlightSerializer(serializers.ModelSerializer):
    uav_name = serializers.ReadOnlyField(source='uav.name')

    class Meta:
        model = models.Flight


class TrackPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrackPoint
