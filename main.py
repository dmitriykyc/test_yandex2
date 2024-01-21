from config import TOKEN
from telebot import TeleBot

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def bot_start(message):
    print('Получена команда /start')
    bot.send_message(message.chat.id, text="Я готов к работе!")



bot.polling()
