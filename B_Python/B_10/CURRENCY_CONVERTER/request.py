import requests
import os
import json
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

base_url = 'http://data.fixer.io/api/'
period = 'latest'
symbols = 'symbols'
access_key = f"?access_key={os.getenv('FX_TOKEN')}"
base = '&base=EUR'

url_currency_ex = f"{base_url}{period}{base}{access_key}"
url_lst_currencies= f"{base_url}{symbols}{access_key}"


class CROSS_RATES:
	def __init__(self, default_currency = 'EUR', 
										exchanged_currency='USD', 
										top_currencies = ['EUR', 'USD', 'GBP', 'JPY', 'CHF'],
										amount = 1.0):


  
		self.current_time = datetime.now()
		self.currency_dict = {}
  
		#self.check_input_currency(currency=default_currency)
		self.parse_data() 
  
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
  

	def parse_data(self):
		self.url = f"http://data.fixer.io/api/latest?access_key={TOKEN}"

		self.currency_dict = requests.get(self.url).json()

#check if input currency is in the keys of the current_dict
	@classmethod
	def check_input_currency(cls, currency: str, currency_dict: dict):
		if currency not in currency_dict['rates'].keys():
			raise AttributeError(f'The input currency {currency} is not in the list of available currencies')
		return True

