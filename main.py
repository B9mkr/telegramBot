import telebot
import subprocess
import datetime
# import csv

bot = telebot.TeleBot('5549761589:AAFRCcJ70srGm5EZ0aQvdqolWYJcHk6yseE')

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, '/today - показує яка сьогодні дата', parse_mode='html')
    bot.send_message(message.chat.id, '/p - робить скріншот екрану на компютері і висилає на телеграм', parse_mode='html')
    bot.send_message(message.chat.id, '/buttonTest ', parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Hello</b>', parse_mode='html')
    subprocess.run(["./test.sh"], shell=True)

@bot.message_handler(commands=['today'])
def today(message):
    answer="Today is " + datetime.datetime.now().strftime("%d %A ; %B (%m) ; %Y")
    bot.send_message(message.chat.id, answer, parse_mode='html')

@bot.message_handler(commands=['p'])
def photo(message):
    photoUrl = "screenshot/" + datetime.datetime.now().strftime("%H%M%S%d%m%Y") + ".png"
    print(f"url: {photoUrl}")
    subprocess.run([f"gnome-screenshot -B -f '{photoUrl}'"], shell=True)
    photo = open(photoUrl, 'rb')
    bot.send_photo(message.chat.id, photo)
    # subprocess.run([f"rm -f '{photoUrl}'"], shell=True)
    photo.close()

# @bot.message_handler(commands=['buttonTest'])
# def buttonTest(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("text", url="google.com"))
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

# def main():

# if __name__ == "__main__":
#     main()

bot.polling(none_stop=True)
