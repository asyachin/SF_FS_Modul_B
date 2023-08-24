import telebot
import os
from dotenv import load_dotenv
from request import CROSS_RATES

 
load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_TOKEN'))

request = CROSS_RATES()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
	help_message = 	'Привет, я бот, который поможет тебе узнать курс валюты!\n'\
 									'/help - поможет тебе разобраться с моим функционалом\n'\
									'/list - покажет тебе список доступных валют\n'\
									'/setdefault - позволит тебе установить валюту по умолчанию\n'\
									'/settop - установка списка валют по умолчанию\n'\
									'/crosscourse - покажет тебе кросс-курс между двумя валютами\n'\

	bot.reply_to(message, help_message)

#function to get all available currencies from set_default_currency method from CROSS_RATES class
@bot.message_handler(commands=['list'])
def send_list(message: telebot.types.Message):
	currencies = request.get_all_currencies()
	bot.reply_to(message, f'Список доступных валют: {currencies}')

									
            
    
  #Для этого введи команду в формате:\n<имя валюты> \n<в какую валюту перевести> \n<количество переводимой валюты>\n '\
 
bot.polling(none_stop=True)