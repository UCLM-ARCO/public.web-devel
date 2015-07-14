# -*- coding: utf-8; mode: python -*-

from django.test import TestCase, Client
from .models import Vehicle


class FormTests(TestCase):
    params = {
        u'brand': "Tesla",
        u'model': "S",
        u'plate': "FSF 0000",
        u'year': 2015,
    }

    def test_form_is_processed(self):
        c = Client()
        response = c.post("/vehicle/create/", self.params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Vehicle.objects.all()), 1)

        v1 = Vehicle.objects.get(plate=self.params['plate'])
        self.assertEqual(v1.model, self.params['model'])
        self.assertEqual(v1.plate, self.params['plate'])
        self.assertEqual(v1.year, self.params['year'])

    def test_form_empty_field_not_valid(self):
        c = Client()
        params = self.params.copy()
        params['brand'] = ""
        response = c.post("/vehicle/create/", params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Vehicle.objects.all().count(), 0)

    def test_form_out_of_range_field_not_valid(self):
        c = Client()
        params = self.params.copy()
        params['year'] = "1900"
        response = c.post("/vehicle/create/", params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Vehicle.objects.all().count(), 0)

    def test_form_duplicated_object_not_created(self):
        v1 = Vehicle(**self.params)
        v1.save()

        self.assertEqual(Vehicle.objects.all().count(), 1)

        c = Client()
        response = c.post("/vehicle/create/", self.params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Vehicle.objects.all().count(), 1)
