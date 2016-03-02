'''
Created on Mar 2, 2016

@author: laurynas
'''

class Investor(object):
    portfolio_list = []

    def __init__(self, username):
        self.username = username
        
    def get_username(self):
        return self.username
    
    def get_latest_portfolio(self):
        return self.portfolio_list[-1]
    
    def get_oldest_portfolio(self):
        return self.portfolio_list[0]
        