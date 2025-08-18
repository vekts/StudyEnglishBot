import telebot
import requests
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import os
from telebot import types

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Ukrainian 🇺🇦', callback_data='ukrainian')
    btn2 = types.InlineKeyboardButton('Russian 🇷🇺', callback_data='russian')
    markup.add(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Spanish 🇪🇸', callback_data='spanish')
    btn4 = types.InlineKeyboardButton('French 🇫🇷', callback_data='french')
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id, "Choose the language:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    response = requests.get('https://random-word-api.vercel.app/api?words=1')
    if response.status_code == 200:
        
        if call.data == 'ukrainian':
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='uk').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='uk').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='uk').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='uk').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")

        elif call.data == 'russian':
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='ru').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='ru').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='ru').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='ru').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")

        elif call.data == 'french':
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='fr').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='fr').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='fr').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='fr').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")

        elif call.data == 'spanish':
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='es').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='es').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='es').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
            response = requests.get('https://random-word-api.vercel.app/api?words=1')
            word = response.json()[0]
            translate = GoogleTranslator(source='en', target='es').translate(word)
            bot.send_message(call.message.chat.id, f"{word} - {translate}")
    else:
        bot.send_message(call.message.chat.id, "DOESN'T WORKING")


bot.infinity_polling()
