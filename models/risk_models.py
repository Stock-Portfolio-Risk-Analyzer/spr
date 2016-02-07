import numpy as np
import pandas as pd
from datautils.yahoo_finance import get_stock_data
from datetime import datetime as dt

def beta(symbol, start_date=dt(year=2009, month=1, day=1), end_date=dt.today(), index_symbol='^GSPC'):

    index_data = get_stock_data(index_symbol, start_date, end_date)
    symbol_data = get_stock_data(symbol, start_date, end_date)

    symbol_returns = symbol_data.pct_change()['Adj Close'].fillna(0)
    index_returns = index_data.pct_change()['Adj Close'].fillna(0)

    # TODO: if stock does not have data since start_date
    
    cov_mat = np.cov(symbol_returns, index_returns)
    beta = cov_mat[0, 1]/cov_mat[1, 1 ]

    return beta

if __name__ == "__main__":
    print beta('AAPL')