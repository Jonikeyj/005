import telebot
import sqlite3

API_TOKEN = "7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI"
bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    username TEXT
)               
''')
conn.commit()

text_message = ""
image_file_id = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username
    
    cursor.execute('''
    SELECT * FROM users WHERE user_id = ?
    ''', (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        print(f"Пользовател {username} уже есть в базе данных!")
    else:
        cursor.execute('''
        INSERT INTO users (user_id, username)
        VALUES (?, ?)
        ''', (user_id, username))   
        conn.commit()           
        print(f"Пользовател {username} успешно добавлен!")
        
    bot.send_message(message.chat.id, "добро пожалывать!")
                       
@bot.message_handler(commands=['send'])
def handle_send(message):
    if message.from_user.id != 5825971888:
        bot.reply_to(message, "FALSE NO YOU")
        return
    bot.send_message(message.chat.id, 'ваш текст')
    bot.register_next_step_handler(message, process_text)

def process_text(message):
    global text_message
    global image_file_id
    text_message = message.text
    bot.send_message(message.chat.id, "картину гони")
    bot.register_next_step_handler(message, process_image)

def process_image(message):
    global image_file_id
    if message.photo:
        image_file_id = message.photo[-1].file_id
        bot.send_message(message.chat.id, "Изабражение полуено Рассылка началась->")
    elif message.text == '/done':
        bot.send_message(message.chat.id, "Рассылка началась->")
    else:
        bot.send_message(message.chat.id, "картину гани")
        return
    
    send_broadcast()
    
def send_broadcast():
    global text_message
    cursor.execute('SELECT user_id FROM users')
    users = cursor.fetchall()

    for user in users:
        user_id = user[0]
        try:
            if image_file_id:
                bot.send_message(user_id, photo=image_file_id, caption=text_message)
            else:
                bot.send_message(user_id, text_message)
        except Exception as e:
            print(f"Ощыбка с ползователем {user_id}: {e}")
    text_message = ""
    image_file_id = None

bot.polling()