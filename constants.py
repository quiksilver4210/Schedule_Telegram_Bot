token = "597454150:AAE7OFsWm0rNjcXVpk9LgLaYmsZjytG7mGY"

import telebot

user_markup_start = telebot.types.ReplyKeyboardMarkup()
user_markup_start.row('Расписание на сегодня', 'Расписание на завтра')
user_markup_start.row('Выбрать день недели')
user_markup_start.row('Расписание звонков')

user_markup_days = telebot.types.ReplyKeyboardMarkup()
user_markup_days.row('Понедельник', 'Четверг')
user_markup_days.row('Вторник', 'Пятница')
user_markup_days.row('Среда', 'Суббота')
user_markup_days.row('Вернуться назад')