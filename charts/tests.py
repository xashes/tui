from django.test import TestCase
from django.urls import resolve
from charts.views import kline
from django.http import HttpRequest

class KlineTest(TestCase):
    def test_root_url_resolves_to_kline_view(self):
        match = resolve('/charts/kline/')
        self.assertEqual(match.func, kline)

    def test_kline_returns_correct_html(self):
        request = HttpRequest()
        response = kline(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Kline</title>', html)
        self.assertTrue(html.endswith('</html>'))
