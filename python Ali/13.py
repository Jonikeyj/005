import telebot
import random

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7188153250:AAFkR1jKkTDaPyfnX2NKhX2B2ToIGEYItRI')

def game(message):
    user_choice = message.text.lower()
    bot_choice = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif user_choice == 'rock' and bot_choice == 'scissors':
        result = "You win! Rock crushes scissors."
    elif user_choice == 'paper' and bot_choice == 'rock':
        result = "You win! Paper covers rock."
    elif user_choice == 'scissors' and bot_choice == 'paper':
        result = "You win! Scissors cuts paper."
    else:
        result = f"You lose! {bot_choice} beats {user_choice}."

    bot.reply_to(message, f"You chose {user_choice}.\nI chose {bot_choice}.\n{result}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() in ['rock', 'paper', 'scissors']:
        game(message)
    else:
        bot.reply_to(message, "Please choose rock, paper, or scissors.")

bot.polling()