from django.test import TestCase, Client


class FormTests(TestCase):
    def test_form_is_processe(self):
        c = Client()
        response = c.post("/print/", {'name': 'peter'})
        expected_content = "name: peter"

        self.assertEqual(response.status_code, 200)
        self.assertIn(expected_content, response.content)
