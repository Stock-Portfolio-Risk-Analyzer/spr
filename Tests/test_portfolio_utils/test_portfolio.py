import unittest
from portfolio_utils.port import Portfolio
from portfolio_utils.investor import Investor

class TestStringMethods(unittest.TestCase):

    def test_get_id(self):
        investor1 = Investor("Shivam")
        investor2 = Investor("Laurynas")        
        portfolio1 = Portfolio(investor1)
        portfolio2 = Portfolio(investor2)
        self.assertFalse(portfolio1.id == portfolio2.id)


if __name__ == '__main__':
    unittest.main()
                