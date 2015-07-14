# -*- coding: utf-8; mode: python -*-

from django.test import TestCase, Client


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
        response = c.post("/valid/", self.params)
        templates = [t.name for t in response.templates]

        self.assertEqual(response.status_code, 200)
        self.assertIn("profile.html", templates)

    def test_form_passwords_mismatch(self):
        params = self.params.copy()
        params[u'confirm-password'] = "other-secret"

        c = Client()
        response = c.post("/valid/", params)
        expected_content = "ERROR: Las contraseñas no coinciden!"

        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_content, response.content)
