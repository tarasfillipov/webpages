from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.template import Template, Context, TemplateSyntaxError

class HttpTest(TestCase):
    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '7webpages test')

    def test_tag(self):
        rendered = Template(
            '{% load my_tags %}'
            '{% note_by_id "1" %}'
        ).render(Context())
        self.assertEqual(rendered, "<p>Hello. This is my first note.</p>")