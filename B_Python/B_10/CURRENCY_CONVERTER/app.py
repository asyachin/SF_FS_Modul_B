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

@bot.message_handler(commands=['list'])
def send_list(message: telebot.types.Message):
    current_chunk = ""
    counter = 0
    currencies_names = request.get_all_currencies()  # Assuming this function retrieves currency names

    for key, value in currencies_names.items():
        current_chunk += f"{key}: {value}\n"
        counter += 1

        if counter == 50:
            bot.send_message(message.chat.id, current_chunk)
            current_chunk = ""
            counter = 0

    if current_chunk:
        bot.send_message(message.chat.id, current_chunk)
    
    bot.reply_to(message, 'Установите валюту по умолчанию с помощью команды /setdefault <код валюты>')
    
@bot.message_handler(commands=['setdefault'])
def set_default(message: telebot.types.Message):
    try:
        parts = message.text.split()  # Split the message text into parts
        if len(parts) == 2:
            currency_code = parts[1]
            # Set the default currency using the request object
            request.set_default_currency(currency_code)
            bot.reply_to(message, f'Валюта по умолчанию установлена на {currency_code}')
        else:
            bot.reply_to(message, 'Вы не указали валюту')
    except Exception as e:
        bot.reply_to(message, f'Произошла ошибка: {str(e)}')


			

									
            
    
  #Для этого введи команду в формате:\n<имя валюты> \n<в какую валюту перевести> \n<количество переводимой валюты>\n '\
 
bot.polling(none_stop=True)