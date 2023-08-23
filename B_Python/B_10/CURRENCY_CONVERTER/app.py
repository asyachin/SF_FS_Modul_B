import telebot
import os
from dotenv import load_dotenv

 
load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_TOKEN'))

@bot.message_handler()
def echo_test(message: telebot.types.Message):
		bot.send_message(message.chat.id, 'hello Alex!')
 
bot.polling(none_stop=True)