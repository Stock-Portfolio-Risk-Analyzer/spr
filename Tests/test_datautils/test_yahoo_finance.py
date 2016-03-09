import unittest
from datautils.yahoo_finance import *


class TestYahooFinance(unittest.TestCase):

    def test_get_current_price(self):
        symbol = 'GOOG'
        current_price = get_current_price(symbol)
        self.assertTrue(type(current_price) is float)
        self.assertGreaterEqual(current_price, 400)

    def test_get_company_name(self):
        symbol = 'GOOG'
        company_name = get_company_name(symbol)
        self.assertEqual(company_name, 'Google Inc.')

    def test_get_company_sector(self):
        symbol = 'GOOG'
        company_sector = get_company_sector(symbol)
        self.assertEqual(company_sector, 'Technology')