import os.path
import telebot

from telebot import types
from datetime import datetime
from sqlite_class import SQLite_class

bot = telebot.TeleBot('2018476544:AAEVO50Pzs5DkVQpW270OW55m3hUw7svoqM')
db = SQLite_class('C:/Users/tig/Desktop/tg bot/tg_bot.db')
#db = SQLite_class('c:/Users/Admin/Desktop/tg/tg_bot.db')

@bot.message_handler(commands=['start','restart'])
def start(message):
    mess = f"Hello {message.from_user.first_name}. To enter the name of the store, enter the command /set_name"       
    bot.send_message(message.chat.id, mess)
    create_manager_folder(f'{message.from_user.first_name} {message.from_user.last_name}')
    
@bot.message_handler(commands=['set_name'])
def set_name2(message):
        bot.register_next_step_handler(message, save_name_floder2)
        bot.send_message(message.chat.id, "Enter store name", reply_markup=types.ReplyKeyboardRemove())

'''        
@bot.message_handler(content_types='text')
def set_name(message):
    if(message.text=='Change store name.'):
        bot.register_next_step_handler(message, save_name_floder)
        bot.send_message(message.chat.id, "Enter store name", reply_markup=types.ReplyKeyboardRemove())
'''

def save_name_floder2(message):
    if (not db.get_last_folder_name(message.from_user.id)):
        db.add_folder_name(message.from_user.id, message.text)        
    else:
        db.update_folder_name(message.from_user.id, message.text)
    create_manager_folder(f'{message.from_user.first_name} {message.from_user.last_name}')
    create_shop_folder(f'{message.from_user.first_name} {message.from_user.last_name}', message.text)   
    bot.send_message(message.from_user.id, f"Photos will be saved for the store: {message.text}. Send a photo.")
    
'''
def save_name_floder(message):
    if (not db.get_last_folder_name(message.from_user.id)):
        db.add_folder_name(message.from_user.id, message.text)        
    else:
        db.update_folder_name(message.from_user.id, message.text)
    create_manager_folder(f'{message.from_user.first_name} {message.from_user.last_name}')
    create_shop_folder(f'{message.from_user.first_name} {message.from_user.last_name}', message.text)
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_set_name = types.KeyboardButton('Change store name.')
    markup_reply.add(item_set_name)
    bot.send_message(message.from_user.id, f"Photos will be saved for the store: {message.text}. Send a photo.",reply_markup=markup_reply)
    '''
  
@bot.message_handler(content_types=['photo'])
def download_picture(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    name_manager =f'{message.from_user.first_name} {message.from_user.last_name}'   
    create_manager_folder(name_manager)
    name_shop_folder = db.get_last_folder_name(message.from_user.id)[0][2]
    create_shop_folder(f'{message.from_user.first_name} {message.from_user.last_name}',name_shop_folder)
    src = f'C:/Users/tig/Desktop/tg bot/{name_manager}/{name_shop_folder}/{message.photo[0].file_id}.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

def create_manager_folder(name_manager):
    if os.path.exists(f'C:/Users/tig/Desktop/tg bot/{name_manager}') == False:
        os.mkdir(f'C:/Users/tig/Desktop/tg bot/{name_manager}')

def create_shop_folder(name_manager,name_shop_folder):
    if os.path.exists(f'C:/Users/tig/Desktop/tg bot/{name_manager}/{name_shop_folder}/') == False:
        os.mkdir(f'C:/Users/tig/Desktop/tg bot/{name_manager}/{name_shop_folder}/')

bot.polling(none_stop=True, interval=0)
