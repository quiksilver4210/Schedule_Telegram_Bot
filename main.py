"""
?
Телеграмм-бот для получения расписания ДВФУ
?
"""

import telebot
token = "597454150:AAE7OFsWm0rNjcXVpk9LgLaYmsZjytG7mGY"

bot = telebot.TeleBot(token)

print(bot.get_me())

def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2})\nRecived message: {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))

    print("Sended message: {0}\n".format(answer))

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Расписание на сегодня','Расписание на завтра')

    bot.send_message(message.from_user.id, 'Welcome', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Расписание на сегодня":
        answer = "Работоспособность 1 кнопки"
        log(message,answer)

        bot.send_message(message.chat.id,answer)
    else:
        answer = "Работоспособность 2 кнопки"
        bot.send_message(message.chat.id,answer)
        log(message,answer)

bot.polling(none_stop=True, interval=0)
