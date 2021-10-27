import os.path
import telebot

from telebot import types
from datetime import datetime

bot = telebot.TeleBot('2018476544:AAEVO50Pzs5DkVQpW270OW55m3hUw7svoqM')

@bot.message_handler(commands=['start','restart'])
def start(message):
    mess = f"Hello {message.from_user.first_name}. To enter the name of the store, enter the command"       
    bot.send_message(message.chat.id, mess)

bot.polling(none_stop=True, interval=0)
