class Investor(object):

    def __init__(self, username):
        self.portfolio_list = []
        self.username = username
        
    def get_username(self):
        return self.username
    
    def get_latest_portfolio(self):
        return self.portfolio_list[-1]
    
    def get_oldest_portfolio(self):
        return self.portfolio_list[0]
        