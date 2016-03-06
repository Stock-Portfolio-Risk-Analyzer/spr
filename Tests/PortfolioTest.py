'''
Created on Mar 6, 2016

@author: laurynas
'''

import unittest
from portfolio_utils.Portfolio import Portfolio
from portfolio_utils.Investor import Investor

class TestStringMethods(unittest.TestCase):

    def test_get_id(self):
        investor1 = Investor("Shivam")
        investor2 = Investor("Laurynas")        
        portfolio1 = Portfolio(investor1)
        portfolio2 = Portfolio(investor2)
        self.assertFalse(portfolio1.get_id() == portfolio2.get_id())
    

if (__name__ == '__main__'):
    unittest.main()
                