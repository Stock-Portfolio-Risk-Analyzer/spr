import unittest
from portfolio_utils.port import Portfolio
from portfolio_utils.investor import Investor
from portfolio_utils.stock import Stock

class TestStringMethods(unittest.TestCase):

    def test_get_id(self):
        investor1 = Investor("Shivam")
        investor2 = Investor("Laurynas")        
        portfolio1 = Portfolio(investor1)
        portfolio2 = Portfolio(investor2)
        self.assertFalse(portfolio1.id() == portfolio2.id)
    
    def test_get_stock_symbol(self):
        stock = Stock("GOOG", 10)
        self.assertEqual(stock.stock_symbol, "GOOG")

    def test_get_number_of_stocks(self):
        stock = Stock("GOOG", 10)
        self.assertEqual(stock.position, 10)
        
if __name__ == '__main__':
    unittest.main()