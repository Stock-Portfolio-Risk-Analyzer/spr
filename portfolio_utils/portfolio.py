from  collections import OrderedDict


class Portfolio(object):

    def __init__(self):
        self.positions = OrderedDict()

    def add_position(self, symbol, quantity):

        self.positions[symbol] = quantity
