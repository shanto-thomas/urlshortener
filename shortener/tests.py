# tests.py in shortener app

from django.test import TestCase
from .models import ShortURL

class ShortURLTest(TestCase):

    def test_url_shortening(self):
        url = ShortURL.objects.create(original_url="https://example.com")
        print(url.short_url)
        self.assertEqual(len(url.short_url), 6)

    def test_redirect(self):
        url = ShortURL.objects.create(original_url="https://example.com")
        response = self.client.get(f'/{url.short_url}/', follow=True)
        self.assertRedirects(response, "https://example.com")
