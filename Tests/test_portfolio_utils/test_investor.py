import unittest
from portfolio_utils.investor import Investor

class TestStringMethods(unittest.TestCase):

    def test_get_username(self):
        investor = Investor("Laurynas")
        self.assertEqual(investor.get_username(), "Laurynas")

if __name__ == '__main__':
    unittest.main()
        