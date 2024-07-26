import telebot
import random
from telebot import types

API_TOKEN = '7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message): 
    # создание кнопок
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/send')
    markup.add(btn1, btn2)

    # отправка сообщения юзеру
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите команду:", reply_markup=markup)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "<b>Доступные команды:</b>\n"
        "/start - начать взаимодействие с ботом\n"
        "/rad - отправить случайное изображение\n"
        "/help - получить помощь и информацию о командах\n"
    )
    bot.reply_to(message, help_text)

# Обработчик команды /rad
@bot.message_handler(commands=['rad'])
def send_random_image(message):
    # первая колонка
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Кнопка 1', url='https://t.me/+UuzMy')
    markup.add(btn1)

    # Вторая и третья кнопки в одной строке под первой кнопкой
    btn2 = types.InlineKeyboardButton('Кнопка 2', url='https://t.me/+Uy')
    btn3 = types.InlineKeyboardButton('Кнопка 3', url='https://t.me/+UMy')
    markup.row(btn2, btn3)

    try:
        # Выбираем случайное число от 0 до 9
        random_index = random.randint(0, 2)
        image_path = f"./img/image{random_index}.jpg"
        
        # Отправляем изображение пользователю
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file, reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

# Обработчик входящих изображений
@bot.message_handler(content_types=['photo', 'video', 'sticker'])
def handle_image(message):
    choice = random.choice(['😍', '👍', '👎', 'Ну такое...']) 
    bot.reply_to(message, choice)

# Обработчик текстовых сообщений
@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Я не хочу разговаривать на эту тему...</b>")

# Запуск бота
bot.polling()