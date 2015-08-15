# -*- coding: utf-8; mode: python; -*-

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
import uuid

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


class DataChanges_view(APIView):
    changes_hash = uuid.uuid4().hex

    @classmethod
    def update_hash(cls):
        cls.changes_hash = uuid.uuid4().hex

    def get(self, request, format=None):
        return Response({'hash': self.changes_hash})


@receiver(post_save)
def on_model_save(**kwargs):
    DataChanges_view.update_hash()
