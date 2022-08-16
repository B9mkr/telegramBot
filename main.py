import telebot
from telebot import types
import subprocess
import datetime
import logging
from config import telebot_token

bot = telebot.TeleBot(telebot_token)

timeOutMessage='Timeouted ... Retrying sending message.'
successSendingMessage='Message sending succefully!'

def sendMessageTelebot(chatId, contentMessage):
    try:
        bot.send_message(chatId, contentMessage, parse_mode='html')
    except Exception as e:
        logging.warning(e)
        logging.warning(timeOutMessage)
    else:
        logging.warning(successSendingMessage)

@bot.message_handler(commands=['help', 'h'])
def start(message):
    sendMessageTelebot(message.chat.id, '/help, /h - Показує які існують команди')
    sendMessageTelebot(message.chat.id, '/b - висилає рівень батареї на компютері')
    sendMessageTelebot(message.chat.id, '/p - робить скріншот екрану на компютері і висилає на телеграм')
    sendMessageTelebot(message.chat.id, 'Після вписання тексту робиться нотатка на комп\'ютері.')

    # bot.send_message(message.chat.id, '/today - показує яка сьогодні дата', parse_mode='html')
    # bot.send_message(message.chat.id, '/p - робить скріншот екрану на компютері і висилає на телеграм', parse_mode='html')
    # bot.send_message(message.chat.id, '/b - висилає рівень батареї на компютері', parse_mode='html')
    # bot.send_message(message.chat.id, 'Після вписання тексту робиться нотатка на комп\'ютері.', parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
    sendMessageTelebot(message.chat.id, '<b>Привіт</b> починаємо працювати.')
    # bot.send_message(message.chat.id, '<b>Привіт</b> починаємо працювати.', parse_mode='html')

@bot.message_handler(commands=['p'])
def photo(message):
    photoUrl = "screenshot/" + datetime.datetime.now().strftime("%H%M%S%d%m%Y") + ".png"
    # print(f"url: {photoUrl}")
    subprocess.run([f"gnome-screenshot -B -f '{photoUrl}'"], shell=True)
    photo = open(photoUrl, 'rb')
    try:
        bot.send_photo(message.chat.id, photo)
    except Exception as e:
        logging.warning(e)
        logging.warning(timeOutMessage)
    else:
        logging.warning(successSendingMessage)
    # subprocess.run([f"rm -f '{photoUrl}'"], shell=True)
    photo.close()

@bot.message_handler(commands=['b'])
# @bot.message_handler(regexp=r'b')
def battery(message):
    # bot.send_message(message.chat.id, '<b>Привіт</b>', parse_mode='html')
    subprocess.run(["./skripts/batery.sh"], shell=True)
    bUrl= "./skripts/batteryNow"
    batteryNow = open(bUrl, 'r')
    # bot.reply_to(message, f"Рівень батареї: {batteryNow.read()}")

    sendMessageTelebot(message.chat.id, f"Рівень батареї: {batteryNow.read()}")

    # try:
    #     bot.send_message(message.chat.id, f"Рівень батареї: {batteryNow.read()}", parse_mode='html')
    # except Exception as e:
    #     logging.warning(e)
    #     logging.warning(timeOutMessage)
    # else:
    #     logging.warning(successSendingMessage)

    batteryNow.close()

@bot.message_handler(content_types=['text'])
def todo(message):
    answer=message.text
    subprocess.run([f"./skripts/test.sh \"{answer}\"  \"{message.date}\""], shell=True)
    try:
        bot.reply_to(message, "Зроблено помітку")
    except Exception as e:
        logging.warning(e)
        logging.warning(timeOutMessage)
    else:
        logging.warning(successSendingMessage)

# @bot.message_handler(commands=['today'])
# def today(message):
#     answer="Today is " + datetime.datetime.now().strftime("%d %A ; %B (%m) ; %Y")
#     bot.send_message(message.chat.id, answer, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def todo(message):
#     try:
#         answer=message.text
#         subprocess.run([f"./test.sh \"{answer}\""], shell=True)
#         bot.send_message(message.chat.id, "Зроблено помітку")
#     except:
#         bot.send_message(message.chat.id, "Something wrong")

# @bot.message_handler(commands=['buttonTest2'])
# def buttonTest2(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("help", url="/help"))
#     bot.send_message(message.chat.id, 'answer', reply_markup=markup)

# @bot.message_handler(commands=['buttonTest'])
# def buttonTest(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     button1 = types.InlineKeyboardButton("button1")
#     button2 = types.InlineKeyboardButton("button2")
#     markup.add(button1, button2)
#     bot.send_message(message.chat.id, 'answer', reply_markup=markup)

# @bot.message_handler(commands=['p'])
# def photo(message):
#     # bot.send_message(message.chat.id, message.text, parse_mode='html')
#     if message.text == "p":
#         photoUrl = "screenshot/" + datetime.datetime.now().strftime("%H%M%S%d%m%Y") + ".png"
#         print(f"url: {photoUrl}")
#         subprocess.run([f"gnome-screenshot -wBi -d 1 -f '{photoUrl}'"], shell=True)
#         photo = open(photoUrl, 'rb')
#         bot.send_photo(message.chat.id, photo)
#         # subprocess.run([f"rm -f '{photoUrl}'"], shell=True)
#         photo.close()

def main():
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.warning(e)
        logging.warning(timeOutMessage)
    else:
        logging.warning('bot polling')

if __name__ == "__main__":
    main()


# - [Telegram Bot на Python / Создания ботов для начинающих за 30 минут - YouTube](https://www.youtube.com/watch?v=HodO2eBEz_8)
