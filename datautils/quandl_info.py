import Quandl as qd
import logbook
from collections import OrderedDict
from datetime import datetime as dt
import pandas
import time

log = logbook.Logger('quandl_info')

# initial call to Quandl. key is stored afterwards
qd.get("NSE/OIL", authtoken="-v_zAsM8GfM8UNnAr6sZ")

def get_stock_data(symbol, start_date=None, end_date=None, db_code="WIKI"):
    """
    blah blah
    """
    if start_date is None:
        start_date = dt(year=1990, month=1, day=1)

    if end_date is None:
        end_date = dt.today()

    if start_date is not None and end_date is not None:
        assert start_date < end_date, "Start date is later than end date."

    log.info("Loading symbol: {}".format(symbol))

    quandl_code = db_code + "/" + symbol
    symbol_data = qd.get(quandl_code, returns="pandas", 
                         trim_start=start_date, trim_end=end_date) 
    return symbol_data

def get_stock_data_multiple(symbols=None, start_date=None, end_date=None, db_code="WIKI"):
    """
    Get OHLC stock data from Quandl for multiple stocks
    :param symbols: list of symbols (strings)
    :param start_date: datetime
    :param end_date: datetime
    :return: OrderedDict of DataFrames of stock data from start_date to end_date
    """
    data = OrderedDict()

    if symbols is not None:
        for symbol in symbols:
            quandl_code = db_code + "/" + symbol
            symbol_data = qd.get(quandl_code, returns="pandas", 
                         trim_start=start_date, trim_end=end_date) 
            data[symbol] = symbol_data

    return data

def get_pct_returns(symbol, start_date=None, end_date=None, col='Adj. Close'):
    """

    :param symbol:
    :param start_date:
    :param end_date:
    :param col: (string) name of column to calculate the pct returns from
    :return:
    """
    data = get_stock_data(symbol, start_date, end_date)[col]

    return data.pct_change().fillna(0)

def get_returns(symbol, start_date=None, end_date=None, col='Adj. Close'):
    """

    :param symbol:
    :param start_date:
    :param end_date:
    :param col:  (string) name of column to calculate the returns from
    :return:
    """
    data = get_stock_data(symbol, start_date, end_date)[col]
    return data.diff().fillna(0)


#For development purposes?
def get_options_data_quandl(symbol=None):
    return list(get_stock_data(symbol).columns.values)

if __name__ == "__main__":
    symbols = "GOOG"
    start_date = dt(year=2015, month=1, day=1)
    end_date = dt(year=2015, month=12, day=31)
    print get_options_data_quandl(symbols)
