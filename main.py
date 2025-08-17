import telebot
import requests
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands = ['start'])
def get_random_word(message):
    response = requests.get('https://random-word-api.vercel.app/api?words=1')
    if response.status_code == 200:
        word = response.json()[0]
        translate = GoogleTranslator(source='en', target='uk').translate(word)
        bot.send_message(message.chat.id, f"{word} - {translate}")
        response = requests.get('https://random-word-api.vercel.app/api?words=1')
        word = response.json()[0]
        translate = GoogleTranslator(source='en', target='uk').translate(word)
        bot.send_message(message.chat.id, f"{word} - {translate}")
        response = requests.get('https://random-word-api.vercel.app/api?words=1')
        word = response.json()[0]
        translate = GoogleTranslator(source='en', target='uk').translate(word)
        bot.send_message(message.chat.id, f"{word} - {translate}")
        response = requests.get('https://random-word-api.vercel.app/api?words=1')
        word = response.json()[0]
        translate = GoogleTranslator(source='en', target='uk').translate(word)
        bot.send_message(message.chat.id, f"{word} - {translate}")
    else:
        bot.send_message(message.chat.id, "DOESN'T WORKING")


bot.infinity_polling()
