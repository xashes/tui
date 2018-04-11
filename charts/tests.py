from django.test import TestCase
from django.urls import resolve
from charts.views import kline
from django.http import HttpRequest

class KlineTest(TestCase):
    def test_root_url_resolves_to_kline_view(self):
        match = resolve('/charts/kline/')
        self.assertEqual(match.func, kline)

    def test_kline_returns_correct_template(self):
        response = self.client.get('/charts/kline/')
        self.assertTemplateUsed(response, 'kline.html')
