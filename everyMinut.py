import telebot
from config import telebot_token

bot = telebot.TeleBot(telebot_token)
bot.send_message(869378031, '<b>Нагадування:</b> пройшла <b><i>Година</i></b>', parse_mode='html')

