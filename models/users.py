import telebot
import random
from models.start import bot
from telebot import types
#сообщения

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '/start':
            bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот готовый вам помочь с html оформлением текста, /help для получения помощи!".format(message.from_user, bot.get_me()))
            #данные пользователя
            name = message.from_user.first_name
            name1 = message.from_user.last_name
            url = message.from_user.username
            iduser = message.from_user.id
            #/данные пользователя
            print("Имя: " + str(name) + " " + str(name1) + "\nСсылка: @" + str(url) + "\nID: " + str (iduser))
        elif message.text == '/help':
            bot.send_message(message.chat.id, "Всё очень просто, вам надо ввести текст с тегами: <u></u>, <i></i>, <b></b>, и я переделаю текст с использованием тегов =)")
        elif message.text == '/lol':
            bot.send_message(message.chat.id, "︻┳ั芫ี┳═─┵")
        elif message.text == '/spam':
            a = 1
            while (a):
                bot.send_message(message.chat.id, "︻┳ั芫ี┳═─┵")
        else:
            try:
                msg = message.text
                bot.send_message(message.chat.id, 'Ваш текст:\n' + str(msg), parse_mode='html')
                print(str(msg) + "\nНаписал @" + message.from_user.username)
            except Exception:
                bot.send_message(message.chat.id, '🤯Что-то пошло не так, проверьте закрыли ли вы все теги, или есть этот тег!\n' + str(msg))
                print(str(msg) + "\nУ рукожопа проблема @" + message.from_user.username)

#︻┳ั芫ี┳═─┵