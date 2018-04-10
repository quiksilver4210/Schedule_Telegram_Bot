"""
?
Телеграмм-бот для получения расписания ДВФУ
?
"""

from datetime import date
from _datetime import datetime

import telebot
import calendar
import constants

bot = telebot.TeleBot(constants.token)

print(bot.get_me())
print("\n")

def log(message, answer):
    print(datetime.now())
    print("Message from {0} {1}. (id = {2})".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id)))
    print("Recieved message: {0}".format(message.text))
    print("Sended message: {0}\n".format(answer))

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=constants.user_markup_start)


@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == "Расписание на сегодня":
        my_date = date.today()
        answer = calendar.day_name[my_date.weekday()]
        log(message,answer)
        bot.send_message(message.chat.id,answer, reply_markup=constants.user_markup_start)

    elif message.text == "Расписание на завтра":
        my_date = date.today()
        answer = calendar.day_name[my_date.weekday()+1]
        bot.send_message(message.chat.id,answer, reply_markup=constants.user_markup_start)
        log(message,answer)

    elif message.text == "Выбрать день недели":
        log(message,"Главное меню")
        bot.send_message(message.chat.id, "Выберите день недели", reply_markup=constants.user_markup_days)

    elif message.text == "Вернуться назад":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=constants.user_markup_start)

    elif message.text == "Расписание звонков":
        bot.send_message(message.from_user.id, "1 пара: 08:30 - 10:00\n"
                                               "2 пара: 10:10 - 11:40\n"
                                               "3 пара: 11:50 - 13:20\n"
                                               "4 пара: 13:30 - 15:00\n"
                                               "5 пара: 15:10 - 16:40\n",reply_markup=constants.user_markup_start)

bot.polling(none_stop=True, interval=0)
