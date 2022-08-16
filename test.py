import telebot
import datetime
from datetime import datetime
from config import telebot_token

bot = telebot.TeleBot(telebot_token)

timeOutMessage='Timeouted ... Retrying sending message.'
successSendingMessage='Message sending succefully!'

def sendMessageTelebot(chatId, contentMessage):
    try:
        bot.send_message(chatId, contentMessage, parse_mode='html')
    except Exception as e:
        print(timeOutMessage)
        # logging.warning(e)
        # logging.warning(timeOutMessage)
    else:
        print(successSendingMessage)
        # logging.warning(successSendingMessage)

@bot.message_handler(commands=['start'])
def start(message):
    sendMessageTelebot(message.chat.id, '<b>Привіт</b> починаємо працювати.')
    # bot.send_message(message.chat.id, '<b>Привіт</b> починаємо працювати.', parse_mode='html')

@bot.message_handler(commands=['info'])
def todo(message):
    dt = datetime.fromtimestamp(message.date)
    year=dt.today().year
    month=dt.today().month
    day=dt.today().day

    hour=dt.today().hour
    minute=dt.today().minute
    second=dt.today().second

    answer=f"year: {year} , month: {month} , day: {day} , hour: {hour} , minute: {minute} , second: {second}"
    bot.reply_to(message, answer)

def main():
    bot.polling(none_stop=True)
    # while(1):

if __name__ == "__main__":
    main()

# bot.reply_to(message, message.text)
