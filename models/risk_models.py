import numpy as np
import pandas as pd
from datautils.yahoo_finance import get_pct_returns
from datetime import datetime as dt

def get_alpha(symbol, start_date=dt(year=2013, month=1, day=1), end_date=dt.today(), symbol_returns=None,
              index_returns=None, index_symbol='^GSPC'):
    """
    Using Jensen's alpha (https://en.wikipedia.org/wiki/Jensen%27s_alpha)
    :param symbol:
    :param start_date:
    :param end_date:
    :param index_symbol:
    :return:
    """
    if symbol_returns is None:
        symbol_returns = get_pct_returns(symbol, start_date, end_date)
    if index_returns is None:
        index_returns = get_pct_returns(index_symbol, start_date, end_date)
    beta = get_beta(symbol, start_date, end_date, index_symbol)
    alpha = np.mean(symbol_returns)-beta*np.mean(index_returns)

    return alpha*100

def get_beta(symbol, start_date=dt(year=2013, month=1, day=1), end_date=dt.today(), index_symbol='^GSPC'):
    """

    :param symbol:
    :param start_date:
    :param end_date:
    :param index_symbol:
    :return:
    """
    symbol_returns = get_pct_returns(symbol, start_date, end_date)
    index_returns = get_pct_returns(index_symbol, start_date, end_date)

    # TODO: if stock does not have data since start_date

    cov_mat = np.cov(symbol_returns, index_returns)
    beta = cov_mat[0, 1]/cov_mat[1, 1 ]

    return beta

def get_volatility(symbol, start_date=dt(year=2013, month=1, day=1), end_date=dt.today(), index_symbol='^GSPC'):
    """
    Standard deviation of returns
    :param symbol:
    :param start_date:
    :param end_date:
    :param index_symbol:
    :return:
    """
    symbol_returns = get_pct_returns(symbol, start_date, end_date)
    index_returns = get_pct_returns(index_symbol, start_date, end_date)
    cov_mat = np.cov(symbol_returns, index_returns)

    volatility = np.sqrt(cov_mat[0, 0])

    return volatility*100

if __name__ == "__main__":
    # print get_beta('AAPL')
    # print get_alpha('FB')
    print get_volatility('FB')