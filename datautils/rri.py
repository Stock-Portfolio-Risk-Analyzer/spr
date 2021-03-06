from datetime import date, timedelta
import numpy as np
import yahoo_finance

"""
API that computes Relative Risk Index for a given Stock or Portfolio
Author - Shivam Gupta (sgupta40@illinois.edu)
	 Rohan Kapoor (rkapoor6@illinois.edu)
"""

def compute_daily_change_for_past_given_days(symbol, number_of_days_back):
	""" 
	Parameter:	symbol -> ticker symbol of the stock (Type -> String)
			number_of_days_back -> number of days back from today 
						for which you want the daily change 
						(Type -> integer)
	return: list of daily change (Type -> list float)
	"""
	start_date = date.today() - timedelta(days=number_of_days_back)
	end_date = date.today()
	symbol_data = yahoo_finance.get_stock_data(symbol, start_date, end_date)
	closing_price = list(symbol_data["Close"])

	daily_change = []
	for i in range(0, len(closing_price)-1):
		daily_change.append(((closing_price[i+1] - closing_price[i])/closing_price[i])*100)
	
	return daily_change

def compute_daily_change_for_range(symbol, start_date, end_date):
	""" 
	Parameter:	symbol -> ticker symbol of the stock (Type -> String)
			start_date, end_date -> range you want to compute on (Type -> String)		

	return: list of daily change (Type -> list float)
	"""
	symbol_data = yahoo_finance.get_stock_data(symbol, start_date, end_date)
	closing_price = list(symbol_data["Close"])

	daily_change = []
	for i in range(0, len(closing_price)-1):
		daily_change.append(((closing_price[i+1] - closing_price[i])/closing_price[i])*100)
	
	return daily_change

def compute_covariance(a, b):
	"""	
	Computes covariance
	Parameter: Two lists of integers/floats
	Return: float 
	"""
	a_mean = (sum(a)/len(a))
	b_mean = (sum(b)/len(b))

	total = 0

	for i in range(0, len(a)):
	    total += ((a[i] - a_mean) * (b[i] - b_mean))

	return (total/(len(a)-1))

def compute_variance(a):
	"""
	Computes Variance
	Parameter: List of integers/floats
	Return: float
	"""
	return np.var(a)

def compute_stock_rri_for_today(symbol, number_of_days_back):
	"""
	Parameter:	symbol -> ticker symbol of the stock (Type -> String)
			number_of_days_back -> 	number of days back from today 
						for which you want rri
						(Type -> integer)

	return: float
	"""
	stock_daily_change  = compute_daily_change_for_past_given_days(symbol, number_of_days_back)
	index_daily_change  = compute_daily_change_for_past_given_days("NYA", number_of_days_back)
	
	covariance_val = compute_covariance(stock_daily_change, index_daily_change)
	vairance_val   = compute_variance(index_daily_change)
	rri = covariance_val/vairance_val
	return (rri + 1)

def compute_stock_rri_for_range(symbol, start_date, end_date):
	"""
	Parameter:	symbol -> ticker symbol of the stock (Type -> String)
			start_date, end_date -> range you want to compute rri on (Type -> String)
	return: float
	"""
	stock_daily_change  = compute_daily_change_for_range(symbol, start_date, end_date)
	index_daily_change  = compute_daily_change_for_range("NYA", start_date, end_date)
	
	covariance_val = compute_covariance(stock_daily_change, index_daily_change)
	vairance_val = compute_variance(index_daily_change)
	rri = covariance_val/vairance_val
	return (rri + 1)

def compute_portfolio_rri_for_today(stock_list, quantity_list, number_of_days_back):
	"""
	Computes RRI for a portfolio
	Parameter:	stock_list -> list of stock tickers
			quantity_list -> quantity of stocks per ticker
			number_of_days_back -> 	number of days back from today 
						for which you want rri
						(Type -> integer)
	Return: float
	"""
	total_rri = 0.0
	total_quantity = 0
	for i in range(len(stock_list)):
		stock_rri = compute_stock_rri_for_today(stock_list[i], number_of_days_back)
		total_rri = total_rri + (stock_rri * quantity_list[i])
		total_quantity = total_quantity + quantity_list[i]

	portfolio_rri = (total_rri / total_quantity)

	return portfolio_rri

def compute_portfolio_rri_for_range(stock_list, quantity_list, start_date, end_date):
	"""
	Computes RRI for a portfolio
	Parameter:	stock_list -> list of stock tickers
			quantity_list -> quantity of stocks per ticker
			start_date, end_date -> range you want to compute rri on (Type -> String)
	Return: float
	"""
	total_rri = 0.0
	total_quantity = 0
	for i in range(len(stock_list)):
		stock_rri = compute_stock_rri_for_range(stock_list[i], start_date, end_date)
		total_rri = total_rri + (stock_rri * quantity_list[i])
		total_quantity = total_quantity + quantity_list[i]

	portfolio_rri = (total_rri / total_quantity)

	return portfolio_rri
