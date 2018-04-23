from django.test import TestCase
from . import local

# Create your tests here.
class LocalTest(TestCase):
    def test_query_stock_table(self):
        stock_df = local.query_stock_table()
        assert len(stock_df) > 3000
