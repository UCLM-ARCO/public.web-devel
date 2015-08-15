from django.test import TestCase, Client


class FormTests(TestCase):
    def test_form_is_processed(self):
        c = Client()

        response = c.post("/save/", {'name': 'peter'})

        self.assertEqual(response.status_code, 302)
        self.assertIn("profile/peter", response.url)
