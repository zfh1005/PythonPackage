import time

class Transaction:
    def __init__(self, amount, date, currency = 'USD', usd_conversion_rate = 1, description = None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description
        
    def amount(self):        
        return self.__amount
    
    def date(self):        
        return self.__date
    
    def currency(self):
        return self.__currency
    
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate
    
    def description(self):
        return self.__description

    def usd(self):
        return self.__amount * self.__usd_conversion_rate

if __name__ == '__main__':
    tt = Transaction(100, time.time(), 'USD', 1.2, 'conversion rate')
    
    
