import Quandl as qd
import logbook
from collections import OrderedDict
from datetime import datetime as dt


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

    quandl_code = database_code + "/" + symbol
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


symbols = ["GOOG", "AAPL"]
start_date = dt(year=2015, month=1, day=1)
end_date = dt(year=2015, month=12, day=31)
print get_stock_data_multiple(symbols, start_date, end_date)

