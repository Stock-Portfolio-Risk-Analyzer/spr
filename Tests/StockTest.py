'''
Created on Mar 6, 2016

'''

import datautils.yahoo_finance as yahoo_finance
import unittest

from portfolio_utils.Portfolio import Portfolio
from portfolio_utils.Investor import Investor
from portfolio_utils.Stock import Stock

class TestStringMethods(unittest.TestCase):

    def test_get_id(self):
        investor1 = Investor("Shivam")
        investor2 = Investor("Laurynas")        
        portfolio1 = Portfolio(investor1)
        portfolio2 = Portfolio(investor2)
        self.assertFalse(portfolio1.get_id() == portfolio2.get_id())
    
    def test_get_stock_symbol(self):
        stock = Stock("GOOG",10)
        self.assertEqual(stock.get_stock_symbol(), "GOOG")
        
    def test_get_number_of_stocks(self):
        stock = Stock("GOOG",10)
        self.assertEqual(stock.get_number_of_stocks(), 10)
        
if (__name__ == '__main__'):
    unittest.main()