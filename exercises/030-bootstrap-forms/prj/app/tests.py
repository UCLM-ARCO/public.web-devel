# -*- coding: utf-8; mode: python -*-

from django.test import TestCase, Client
from urlparse import urlparse


class FormTests(TestCase):
    params = {
        u'username': 'jonny',
        u'firstname': 'Jonh',
        u'lastname': 'Doe',
        u'location': 'spain',
        u'color': "#554466",
        u'birth_date': "05/06/07",
        u'password': "secret",
        u'confirm-password': "secret"}

    def test_form_is_processed(self):
        c = Client()
        response = c.post("/register/", self.params)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response['Location']).path, '/')

    def test_form_passwords_mismatch(self):
        params = self.params.copy()
        params[u'confirm-password'] = "other-secret"

        c = Client()
        response = c.post("/register/", params)
        expected_content = "ERROR: Las contraseñas no coinciden!"

        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_content, response.content)
