import requests
import os
import json
from dotenv import load_dotenv



load_dotenv()

URL = 'http://data.fixer.io/api/'
TOKEN = os.getenv('FIXER_TOKEN')

head = {'Authorization':'token {}'.format(TOKEN)}

response = requests.get(URL + 'symbols', headers=head)

