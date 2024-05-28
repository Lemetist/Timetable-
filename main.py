import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Расписание звонков')
    markup.add(itembtn1)

    schedule = (
        "Расписание звонков для Авангардная улица, 5\n\n"
        "1 пара: 08:00 — 09:35 (10 минут)\n"
        "      Перемена: 08:45 — 08:50 (5 минут)\n\n"
        "2 пара: 09:45 — 11:20 (30 минут)\n"
        "      Перемена: 10:30 — 10:35 (5 минут)\n\n"
        "3 пара: 11:50 — 13:25 (30 минут)\n"
        "      Перемена: 12:35 — 12:40 (5 минут)\n\n"
        "4 пара: 13:55 — 15:30 (10 минут)\n"
        "      Перемена: 14:40 — 14:45 (5 минут)\n\n"
        "5 пара: 15:40 — 17:15 (10 минут)\n"
        "      Перемена: 16:25 — 16:30 (5 минут)\n\n"
        "6 пара: 17:25 — 19:00\n"
        "      Перемена: 18:10 — 18:15 (5 минут)"
    )

    bot.send_message(message.chat.id, schedule, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Расписание звонков':
        send_welcome(message)

bot.polling()