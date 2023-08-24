import requests
import os
import json
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

class CROSS_RATES:
	def __init__(self, default_currency = 'EUR', 
										exchanged_currency='USD', 
										top_currencies = ['EUR', 'USD', 'GBP', 'JPY', 'CHF'],
										amount = 1.0):

		self.current_time = datetime.now()
		self.currency_dict = {}

		self.get_data() 
  
		self.default_currency = default_currency
		self.exchanged_currency = exchanged_currency
		self.top_currencies = top_currencies
		self.amount = amount
		self.currency = None
  
		#check all input currencies if they are valid by check_input_currency method
		self.check_input_currency(default_currency, self.currency_dict)
		self.check_input_currency(exchanged_currency, self.currency_dict)
		for currency in top_currencies:
			self.check_input_currency(currency, self.currency_dict)
  

	def get_data(self):
		self.base_url = 'http://data.fixer.io/api/'
		self.period = 'latest'
		self.symbols = 'symbols'
		self.access_key = f"?access_key={os.getenv('FX_TOKEN')}"
		self.base = '&base=EUR'

		self.url_currency_ex = f"{self.base_url}{self.period}{self.base}{self.access_key}"
		self.url_lst_currencies= f"{self.base_url}{self.symbols}{self.access_key}"

		self.list_currencies = requests.get(self.url_lst_currencies).json()
		self.currency_dict = requests.get(self.url_currency_ex).json()

#check if input currency is in the keys of the current_dict
	@classmethod
	def check_input_currency(cls, currency: str, currency_dict: dict):
		if currency not in currency_dict['rates'].keys():
			raise AttributeError(f'The input currency {currency} is not in the list of available currencies')
		return True

#check if input amount is a number
	@classmethod
	def check_input_amount(cls, amount: float):
		if not isinstance(amount, (int, float)):
			raise AttributeError(f'The input amount {amount} is not a number')
		return True

#method to return a list of all available currencies from dictionary list_currencies
	def get_all_currencies(self):
		return self.list_currencies['symbols']

#method to set default currency
	def set_default_currency(self, currency: str):
		self.check_input_currency(currency, self.currency_dict)
		self.default_currency = currency
		return self.default_currency





