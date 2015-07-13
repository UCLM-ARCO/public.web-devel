from django.test import TestCase, Client


class HelloTest(TestCase):
    def test_template_is_rendered(self):
        c = Client()
        response = c.get("/hello/bob/")
        expected_content = "Hello <b>Bob</b>!"

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, expected_content)
