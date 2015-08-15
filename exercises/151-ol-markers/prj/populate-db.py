#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

from django.contrib.auth.models import User
from eventlog import models
from django.utils import timezone
from datetime import timedelta
import random
import uuid
import factory


model_names = ['CSIRO Mantis', 'V-TOL Arrow', 'Berkut', 'Proton', 'Dragonfly Tango']
flight_status = [
    models.Flight.STATUS_OK,
    models.Flight.STATUS_ISSUES,
    models.Flight.STATUS_FAILURE,
]


class UAVStub(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UAV

    @factory.lazy_attribute
    def name(self):
        name = random.choice(model_names)
        model_names.remove(name)

        try:
            count = int(name.split()[-1]) + 1
            next_name = " ".join(name.split()[:-1])
        except ValueError:
            count = 2
            next_name = name

        model_names.append(next_name + " {}".format(count))
        return name


last_flight = None


class FlightStub(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Flight

    uav = factory.SubFactory(UAVStub)

    @factory.lazy_attribute
    def number(self):
        global last_flight
        last_flight = str(uuid.uuid4())[9:18].upper()
        return last_flight

    @factory.lazy_attribute
    def status(self):
        return random.choice(flight_status)


last_ts = timezone.now()
last_used_flight = None
starting_lat = 0
starting_lon = 0


class TrackPointStub(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TrackPoint

    flight = factory.SubFactory(FlightStub)

    @factory.sequence
    def timestamp(n):
        global last_ts
        global last_used_flight
        global starting_lat
        global starting_lon

        last_ts += timedelta(minutes=n)

        if last_flight != last_used_flight:
            last_used_flight = last_flight
            starting_lat = random.randint(-50, 50)
            starting_lon = random.randint(-25, 25)

            days = random.randint(1, 20)
            last_ts += timedelta(days=days)

        return last_ts

    @factory.lazy_attribute
    def latitude(self):
        return starting_lat + random.choice([1, -1]) * random.random() * 5

    @factory.lazy_attribute
    def longitude(self):
        return starting_lon + random.choice([1, -1]) * random.random() * 5

    altitude = 100


user = User.objects.create_user("user", "user@example.com", "secret")
user.save()
print "User", user.username, "created"

for i in range(3):
    uav = UAVStub()

    for j in range(random.randint(1, 6)):
        flight = FlightStub(uav=uav)
        TrackPointStub.reset_sequence()

        for k in range(random.randint(5, 15)):
            point = TrackPointStub(flight=flight)
            print uav.name, flight.number, [point.latitude, point.longitude]
            point.save()
