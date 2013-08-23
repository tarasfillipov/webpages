from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.template import Template, Context, TemplateSyntaxError
from models import Note
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

    def test_post(self):
        data = dict()
        data['text'] = 'hello hello'

        response = self.client.post(reverse('add'), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data['text'])

        note = Note.objects.get(pk=2)
        self.assertEqual(note.text, 'hello hello')

    def test_context_processor(self):
        response = self.client.get('/')
        amount = Note.objects.all().count()
        self.assertEquals(
            response.context['amount'],amount)