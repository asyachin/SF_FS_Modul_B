import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class CurrencyConverter:
    def __init__(self, base='EUR', symbols=['USD','NOK','PLN','GBP','DKK'], target='USD', amount=1, period=datetime.today().strftime('%Y-%m-%d')):
        #self.base_url = 'http://data.fixer.io/api/'
        self.base_url = "https://api.apilayer.com/currency_data/"
        self.__access_key = os.getenv('FX_TOKEN')
        self.base = base
        self.symbols = ",".join(symbols)
        self.period = period
        self.amount = amount
        self.target = target
        self.available_currencies, self.currencies_code, self.currencies_name = self.get_list_currecies()
        
        self.exchange_rate_url = None
        self.get_list_currecies()

    def set_base_currency(self, base):
        if base in self.currencies_code:
            self.base = base
        else:
            raise ValueError(f"Currency {base} is not available")
        
    def get_base_currency(self):
        return self.base

    def set_top_currencies(self, symbols):
        self.symbols = symbols
        
    def get_top_currencies(self):
        return self.symbols

    def set_target_currency(self, target):
        if target in self.currencies_code:
            self.target = target
        else:
            raise ValueError(f"Currency {target} is not available")
        
    def get_target_currency(self):
        return self.target

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount
    
#Convert one currency to another.
    def get_currency_rate(self):
        self.exchange_rate_url = f"{self.base_url}convert&to={self.target}&from={self.base}&amount={self.amount}&date={self.period}?apikey={self.__access_key}"
        response = requests.get(self.exchange_rate_url)
        return response.json()

#Returns all available currencies.
    def get_list_currecies(self):
        self.list_currencies_url = f"{self.base_url}list?apikey={self.__access_key}"
        response = requests.get(self.list_currencies_url)
        self.available_currencies = response.json().get('currencies')
        self.currencies_code, self.currencies_name = self.available_currencies.keys(), self.available_currencies.values()
        return self.available_currencies, self.currencies_code, self.currencies_name 

#Get the most recent exchange rate data.
    def get_most_recent_currencies(self):
        self.most_recent_url = f"{self.base_url}live?source={self.base}&currencies={self.symbols}&apikey={self.__access_key}"
        response = requests.get(self.most_recent_url)
        return response.json().get('quotes')

