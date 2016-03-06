from collections import OrderedDict
import itertools
from investor import *

class Portfolio(object):
    stock_list = []
    RRI = 0.0
    total_value = 0.0
         
    def __init__(self, investor):
        self.investor = investor.get_username()
        self.id = str(self.investor) + "_" + str(id(self))

    def set_total_value(self):
        self.total_value = self.compute_total_value()
        
    def compute_total_value(self):
        value = 0
        for stock in self.stock_list:
            value += stock.get_current_price()
        return value
    
    def get_total_value(self):
        return self.total_value
    
if __name__ == '__main__':
    port1 = Portfolio(Investor("Shivam"))
    print port1.id
    port2 = Portfolio(Investor("Laurynas"))
    print port2.id
