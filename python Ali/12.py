import requests
import telebot
import json 
from telebot import types

API_TOKEN = '7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcom(message):

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/shy')
    btn2 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/start')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Добро пожаловать! Выберите команду:", reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_txt = (
        "<b>Доступные каманды:</b>\n"
        "/help - Ввыводит все камманды\n"
        "/start - Запустит бота\n"
        "/shy - отправка случайной картинки\n"

    )
    bot.reply_to(message, help_txt)

@bot.message_handler(commands=['shy'])
def get_random_joke(message):
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    joke_data = json.loads(response.text)
    bot.send_message(message.chat.id, joke_data['setup'])
    bot.send_message(message.chat.id, joke_data['punchline'])


bot.polling()