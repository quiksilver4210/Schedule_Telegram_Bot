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
import sqlite3



bot = telebot.TeleBot(constants.token)

print(bot.get_me())
print("\n")


def log(message):
    print(datetime.now())
    print("Message from {0} {1}. (id = {2})".format(message.from_user.first_name, message.from_user.last_name,
                                                    str(message.from_user.id)))
    print("Recieved message: {0}\n".format(message.text))



@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Приятного пользования', reply_markup=constants.user_markup_start)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = ""
    if message.text == "Расписание на сегодня":
        my_date = date.today()
        answer = calendar.day_name[my_date.weekday()]

    if message.text == "Расписание на завтра":
        my_date = date.today()
        answer = calendar.day_name[(my_date.weekday() + 1) % 7]

    elif message.text == "Выбрать день недели":
        bot.send_message(message.chat.id, "Выберите день недели", reply_markup=constants.user_markup_days)

    elif message.text == "Вернуться назад":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=constants.user_markup_start)

    elif message.text == "Расписание звонков":
        answer = constants.schedule_bell
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Какая неделя":
        import datetime
        week = datetime.datetime.utcnow().isocalendar()[1]
        answer = ""
        if (week%2)==0:
            answer = "Четная"
        else:
            answer = "Нечетная"
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    if message.text == "Понедельник" or (answer == "Monday"):
        request = "select * from Monday"
        answer = constants.fromSQL(request)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Вторник" or (answer == "Tuesday"):
        request = "select * from Tuesday"
        answer = constants.fromSQL(request)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Среда" or (answer == "Wednesday"):
        request = "select * from Wednesday"
        answer = constants.fromSQL(request)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Четверг" or (answer == "Thursday"):
        request = "select * from Thursday"
        answer = constants.fromSQL(request)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Пятница" or (answer == "Friday"):
        request = "select * from Friday"
        answer = constants.fromSQL(request)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Суббота" or (answer == "Saturday"):
        request = "select * from Saturday"
        answer = constants.fromSQL(request)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    log(message)

bot.polling(none_stop=True, interval=0)
