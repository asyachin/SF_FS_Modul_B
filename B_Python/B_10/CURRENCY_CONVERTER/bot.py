import telebot
import os
from dotenv import load_dotenv
from url_config import CurrencyConverter

cross_rate = CurrencyConverter()

load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def help_message(message):
    bot.reply_to(message, "Hello! I'm a currency converter bot. \n"
                          "To get started, enter the command /convert \n"
                          "and follow the instructions.\n"
                          "To show the list of available currencies, enter the command /values")

@bot.message_handler(commands=['convert'])
def convert_message(message):
    bot.reply_to(message, "Enter the currency you want to convert from:")
    bot.register_next_step_handler(message, get_base_currency)

def get_base_currency(message):
    try:
        cross_rate.set_base_currency(message.text.upper())
        bot.reply_to(message, "Enter the currency you want to convert to:")
        bot.register_next_step_handler(message, get_target_currency)
    except ValueError as e:
        bot.reply_to(message, f"Invalid currency. Try again. {e}")

def get_target_currency(message):
    try:
        cross_rate.set_target_currency(message.text.upper())
        bot.reply_to(message, "Enter the amount:")
        bot.register_next_step_handler(message, get_amount)
    except ValueError as e:
        bot.reply_to(message, f"Invalid currency. Try again. {e}")

def get_amount(message):
    try:
        cross_rate.set_amount(message.text)
        bot.reply_to(message, f"Exchange rate of {cross_rate.get_amount()} {cross_rate.get_base_currency()} is {cross_rate.get_currency_rate()['result']}{cross_rate.get_target_currency()}")
    except ValueError as e:
        bot.reply_to(message, f"Invalid currency. Try again. {e}")
        
@bot.message_handler(commands=['values'])
def values_message(message):
    #output all available currencies as a string key - value
    av_currencies = "\n".join([f"{key} : {value}" for key, value in cross_rate.available_currencies.items()])
    bot.reply_to(message, f"Available currencies:\n {av_currencies}")

bot.polling()

