from datetime import date, timedelta
import numpy as np
import yahoo_finance

"""
http://www.fool.com/knowledge-center/2015/09/10/how-to-calculate-the-beta-coefficient-for-a-single.aspx
"""

def compute_daily_change(symbol, number_of_days_back):
	start_date = date.today() - timedelta(days=number_of_days_back)
	end_date = date.today()
	symbol_data = yahoo_finance.get_stock_data(symbol, start_date, end_date)
	closing_price = list(symbol_data["Close"])

	daily_change = []
	for i in range(0, len(closing_price)-1):
		daily_change.append(((closing_price[i+1] - closing_price[i])/closing_price[i])*100)
	
	return daily_change


def compute_covariance(a, b):
    a_mean = sum(a)/len(a)
    b_mean = sum(b)/len(b)

    total = 0

    for i in range(0, len(a)):
        total += ((a[i] - a_mean) * (b[i] - b_mean))

    return total/(len(a)-1)

def compute_variance(a):
	return np.var(a)

def compute_stock_rri(symbol, number_of_days_back):
	stock_daily_change = compute_daily_change(symbol, number_of_days_back)
	index_daily_change  = compute_daily_change("NYA", number_of_days_back)
	
	covariance_val = compute_covariance(stock_daily_change, index_daily_change)
	vairance_val = compute_variance(index_daily_change)
	rri = covariance_val/vairance_val
	return (rri + 1)

def compute_portfolio_rri(stock_list, quantity_list):
	for i in range(len(stock_list)):
		compute_stock_rri()