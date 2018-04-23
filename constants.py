import telebot
import sqlite3

token = "597454150:AAE7OFsWm0rNjcXVpk9LgLaYmsZjytG7mGY"

schedule_bell=   "1 пара: 08:30 - 10:00\n"\
                +"2 пара: 10:10 - 11:40\n"\
                +"3 пара: 11:50 - 13:20\n"\
                +"4 пара: 13:30 - 15:00\n"\
                +"5 пара: 15:10 - 16:40\n"


user_markup_start = telebot.types.ReplyKeyboardMarkup()
user_markup_start.row('Расписание на сегодня', 'Расписание на завтра')
user_markup_start.row('Выбрать день недели')
user_markup_start.row('Расписание звонков')
user_markup_start.row('Какая неделя')

user_markup_days = telebot.types.ReplyKeyboardMarkup()
user_markup_days.row('Понедельник', 'Четверг')
user_markup_days.row('Вторник', 'Пятница')
user_markup_days.row('Среда', 'Суббота')
user_markup_days.row('Вернуться назад')


def fromSQL(request):
    import datetime
    week = datetime.datetime.now().isocalendar()[1]
    if (week % 2) == 0:
        position = 1
    else:
        position = 0
    answer =""
    conn = sqlite3.connect('schedule.sqlite')
    c = conn.cursor()
    c.execute(request)
    row = c.fetchone()
    while row is not None:

        answer = answer + ("------------------------------------------------\n"
                           + str(row[0]) + " ПАРА \n"
                           + "\n"
                           + "Предмет: " + str(row[1]).split("/")[position]
                           + "\n"
                           + "Преподаватель: " + str(row[2]).split("/")[position]
                           + "\n" + "Аудитория: " + str(row[3]).split("/")[position]
                           + "\n" + "------------------------------------------------\n")
        row = c.fetchone()
    return answer
