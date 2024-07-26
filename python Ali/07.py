import telebot
import random

# import speech_recognition as sr
# from pydub import AudioSegment
# import os 


API_TOKEN = '7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcom(message):
    bot.reply_to(message, f'Добро пожоловать в бот "bot name" v0.1')

@bot.message_handler(commands=['help'])
def send_help(message):
    help_txt = (
        "<b>Доступные каманды:</b>\n"
        "/help - Ввыводит все камманды\n"
        "/start - Запустит бота\n"
        "/rand - отправка случайной картинки\n"

    )
    bot.reply_to(message, help_txt)

@bot.message_handler(commands=['rand'])
def rand_img(message):
    try:
        random_index = random.randint(0,1)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"false {e}")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        voice_ogg_path = "voice.ogg"
        voice_wav_path = "voice.wav"
        
        with open(voice_ogg_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        audio = AudioSegment.from_ogg(voice_ogg_path)
        audio.export(voice_wav_path, format="wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile(voice_wav_path) as source:
            audio_date = recognizer.record(source)
            text = recognizer.recognize_google(audio_date, language="ru-RU")
            bot.reply_to(message, f"вы сказали {text}")

        os.remove(voice_ogg_path)
        os.remove(voice_wav_path)
    except Exception as e:
        bot.reply_to(message, f"ощыбка! {e}")
                
@bot.message_handler(content_types=['photo', 'video', 'sticker', 'message'])
def reaction_message(message):
    choice = random.choice(['😎', '😐', '😍', '💩'])
    bot.reply_to(message, choice)

@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Я не хочу разгаваривать на эту тему</b>")



bot.polling()