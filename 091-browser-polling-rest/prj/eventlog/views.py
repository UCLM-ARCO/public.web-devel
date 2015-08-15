# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

import models
import serializers


def index(request):
    return render(request, "eventlog.html")


class UAV_viewset(viewsets.ModelViewSet):
    queryset = models.UAV.objects.all()
    serializer_class = serializers.UAVSerializer


class Flight_viewset(viewsets.ModelViewSet):
    queryset = models.Flight.objects.all()
    serializer_class = serializers.FlightSerializer

    def create(self, request):
        uav = models.UAV.objects.get_or_create(name=request.data['uav'])[0]
        uav.save()
        flight = models.Flight(uav=uav, number=request.data['flight'], status=2)
        flight.save()

        return Response()


class TrackPoint_viewset(viewsets.ModelViewSet):
    queryset = models.TrackPoint.objects.all()
    serializer_class = serializers.TrackPointSerializer
