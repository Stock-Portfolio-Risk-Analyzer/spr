import ystockquote
import pandas as pd
import logbook
import unittest
import pandas_datareader as datareader
from collections import OrderedDict
from datetime import datetime as dt

log = logbook.Logger('yahoo_finance')


def get_stock_data_yahoo(symbols=None, start_date=None, end_date=None):
    """
    :param symbols: list of symbols
    :param start_date: datetime
    :param end_date: datetime
    :return: OrderedDict of DataFrames of stock data from start_date to end_date
    """
    if start_date is None:
        start_date = dt(year=1990, month=1, day=1)

    if end_date is None:
        end_date = dt.today()

    if start_date is not None and end_date is not None:
        assert start_date < end_date, "Start date is later than end date."

    data = OrderedDict()

    if symbols is not None:
        for symbol in symbols:
            log.info("Loading symbol: {}".format(symbol))
            symbol_data = datareader(symbol, 'yahoo', start_date, end_date)
            data[symbol] = symbol_data

    return data


def get_options_data_yahoo(symbols=None, start_date=None, end_date=None):
    raise NotImplementedError("")

def get_current_price(symbol):
    return float(ystockquote.get_price(symbol))


class TestYahooFinance(unittest.TestCase):

    def test_get_current_price(self):
        symbol = 'GOOG'
        current_price = get_current_price(symbol)
        self.assertTrue(type(current_price) is float)
        self.assertGreaterEqual(current_price, 400)

if __name__ == "__main__":
    unittest.main()