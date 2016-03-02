'''
Created on Mar 2, 2016

@author: sgupta40 & tamulev2
'''

import datautils.yahoo_finance as yahoo_finance

class Stock(object):
    stock_symbol = ''
    number_of_stocks = 0
    current_price = 0.0
    
    def __init__(self, stock_symbol, number_of_stocks):
        self.stock_symbol = stock_symbol
        self.number_of_stocks = number_of_stocks
        self.current_price = yahoo_finance.get_current_price(stock_symbol)
    def get_current_price(self):
        return self.current_price

if (__name__ == '__main__'):
    print("Testing")