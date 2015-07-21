# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from rest_framework import generics

import models
import serializers


def index(request):
    return render(request, "event-list.html")


class UAVAPIList(generics.ListCreateAPIView):
    queryset = models.UAV.objects.all()
    serializer_class = serializers.UAVSerializer


class UAVAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UAV.objects.all()
    serializer_class = serializers.UAVSerializer


class FlightAPIList(generics.ListCreateAPIView):
    queryset = models.Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class FlightAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class TrackPointAPIList(generics.ListCreateAPIView):
    queryset = models.TrackPoint.objects.all()
    serializer_class = serializers.TrackPointSerializer


class TrackPointAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TrackPoint.objects.all()
    serializer_class = serializers.TrackPointSerializer
