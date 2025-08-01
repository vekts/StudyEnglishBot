import telebot
import requests
from deep_translator import GoogleTranslator

TOKEN = '7889841829:AAG5EP5hqIlk5cCOC5_ohjrcTszcPtuaOHQ'
bot = telebot.TeleBot(TOKEN)


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
