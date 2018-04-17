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


def log(message, answer):
    print(datetime.now())
    print("Message from {0} {1}. (id = {2})".format(message.from_user.first_name, message.from_user.last_name,
                                                    str(message.from_user.id)))
    print("Recieved message: {0}".format(message.text))
    print("Sended message: {0}\n".format(answer))


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Welcome', reply_markup=constants.user_markup_start)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = ""
    if message.text == "Расписание на сегодня":
        my_date = date.today()
        answer = calendar.day_name[my_date.weekday()]

        log(message, answer)


    elif message.text == "Расписание на завтра":
        my_date = date.today()
        answer = calendar.day_name[(my_date.weekday() + 1) % 7]

        log(message, answer)

    elif message.text == "Выбрать день недели":
        log(message, "Главное меню")
        bot.send_message(message.chat.id, "Выберите день недели", reply_markup=constants.user_markup_days)

    elif message.text == "Вернуться назад":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=constants.user_markup_start)

    elif message.text == "Расписание звонков":
        answer = constants.schedule_bell
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    if message.text == "Понедельник" or (answer == "Monday"):
        conn = sqlite3.connect('schedule.sqlite')
        c = conn.cursor()
        c.execute('select * from Monday')
        row = c.fetchone()
        answer = constants.fromSQL(c, row)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Вторник" or (answer == "Tuesday"):
        conn = sqlite3.connect('schedule.sqlite')
        c = conn.cursor()
        c.execute('select * from Tuesday')
        row = c.fetchone()
        answer = constants.fromSQL(c, row)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Среда" or (answer == "Wednesday"):
        conn = sqlite3.connect('schedule.sqlite')
        c = conn.cursor()
        c.execute('select * from Wednesday')
        row = c.fetchone()
        answer = constants.fromSQL(c, row)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Четверг" or (answer == "Thursday"):
        conn = sqlite3.connect('schedule.sqlite')
        c = conn.cursor()
        c.execute('select * from Thursday')
        row = c.fetchone()
        answer = constants.fromSQL(c, row)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Пятница" or (answer == "Friday"):
        conn = sqlite3.connect('schedule.sqlite')
        c = conn.cursor()
        c.execute('select * from Friday')
        row = c.fetchone()
        answer = constants.fromSQL(c, row)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)

    elif message.text == "Суббота" or (answer == "Saturday"):
        conn = sqlite3.connect('schedule.sqlite')
        c = conn.cursor()
        c.execute('select * from Saturday')
        row = c.fetchone()
        answer = constants.fromSQL(c, row)
        bot.send_message(message.from_user.id, answer, reply_markup=constants.user_markup_start)


bot.polling(none_stop=True, interval=0)
