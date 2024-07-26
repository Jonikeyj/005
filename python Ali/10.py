import telebot 
import sqlite3
 
API_TOKEN = '7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы для хранения информации о пользователях
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT
)
''')
conn.commit()

# Глобальные переменные
text_message = ""
image_file_id = None

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Проверка, есть ли уже пользователь в базе данных
    cursor.execute('''
    SELECT * FROM users WHERE user_id = ?
    ''', (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        print(f"Пользователь {username} уже есть в базе данных.")
    else:
        # Запись информации о пользователе в базу данных
        cursor.execute('''
        INSERT INTO users (user_id, username)
        VALUES (?, ?)
        ''', (user_id, username))
        conn.commit()
        print(f"Успешно добавлен пользователь {username}.")

    bot.send_message(message.chat.id, "Добро пожаловать!")

# Обработчик команды /send
@bot.message_handler(commands=['send'])
def handle_send(message):
    # Проверка, является ли отправитель администратором
    if message.from_user.id != 5825971888:
        bot.reply_to(message, "У вас нет прав для использования этой команды.")
        return

    # Сохраняем текст сообщения и изображение, если есть
    bot.send_message(message.chat.id, "Отправьте текст сообщения:")
    bot.register_next_step_handler(message, process_text)

def process_text(message):
    global text_message
    text_message = message.text
    bot.send_message(message.chat.id, "Отправьте изображение (если есть), или просто напишите /done, чтобы завершить.")
    bot.register_next_step_handler(message, process_image)

def process_image(message):
    global image_file_id
    if message.photo:
        image_file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, "Изображение получено. Рассылка будет выполнена.")
    elif message.text == '/done':
        bot.send_message(message.chat.id, "Рассылка завершена.")
    else:
        bot.send_message(message.chat.id, "Отправьте изображение или напишите /done.")
        return

    # Запуск рассылки сообщений
    send_broadcast()

def send_broadcast():
    global image_file_id, text_message
    # Получаем всех пользователей из базы данных
    cursor.execute('SELECT user_id FROM users')
    users = cursor.fetchall()
    
    for user in users:
        user_id = user[0]
        try:
            if image_file_id:
                bot.send_photo(user_id, photo=image_file_id, caption=text_message)
            else:
                bot.send_message(user_id, text_message)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

    # Сброс глобальных переменных после рассылки
    image_file_id = None
    text_message = ""

@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Я не хочу разговаривать на эту тему...</b>")

# Запуск бота
bot.polling()