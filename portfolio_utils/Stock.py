import datautils.yahoo_finance as yahoo_finance

class Stock(object):

    def __init__(self, stock_symbol, position):
        self.stock_symbol = stock_symbol
        self.position = position
        self.current_price = yahoo_finance.get_current_price(stock_symbol)
