# -*- coding: utf-8; mode: python -*-

from django.test import TestCase, Client
from .models import Vehicle

REDIRECT = 302
OK = 200


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

        self.assertEqual(response.status_code, REDIRECT)
        self.assertEqual(Vehicle.objects.all().count(), 1)

        v1 = Vehicle.objects.get(plate=self.params['plate'])
        self.assertEqual(v1.model, self.params['model'])
        self.assertEqual(v1.plate, self.params['plate'])
        self.assertEqual(v1.year, self.params['year'])

    def test_form_empty_field_not_valid(self):
        c = Client()
        params = self.params.copy()
        params['brand'] = ""
        response = c.post("/vehicle/create/", params)

        self.assertEqual(response.status_code, OK)
        self.assertEqual(Vehicle.objects.all().count(), 0)

    def test_form_out_of_range_field_not_valid(self):
        c = Client()
        params = self.params.copy()
        params['year'] = "1900"
        response = c.post("/vehicle/create/", params)

        self.assertEqual(response.status_code, OK)
        self.assertEqual(Vehicle.objects.all().count(), 0)

    def test_form_duplicated_object_not_created(self):
        v1 = Vehicle(**self.params)
        v1.save()

        self.assertEqual(len(Vehicle.objects.all()), 1)

        c = Client()
        response = c.post("/vehicle/create/", self.params)

        self.assertEqual(Vehicle.objects.all().count(), 1)
        self.assertEqual(response.status_code, OK)

    def test_list_items(self):

        import factory

        class VehicleStub(factory.django.DjangoModelFactory):
            class Meta:
                model = Vehicle

            brand = factory.Sequence(lambda n: "Brand {}".format(n))
            model = factory.Sequence(lambda n: "Model {}".format(n))
            plate = factory.Sequence(lambda n: "ABC {:04d}".format(n))
            year = 2015

        vehicles = [VehicleStub(), VehicleStub(), VehicleStub()]

        c = Client()
        response = c.post("/vehicle/list/")

        self.assertEqual(response.status_code, OK)
        for v in vehicles:
            self.assertIn(v.brand, response.content)
            self.assertIn(v.model, response.content)
            self.assertIn(v.plate, response.content)
