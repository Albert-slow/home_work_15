from telebot import types


def btn_number():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton('Отправить номер', request_contact=True)
    kb.add(number)
    return kb


def btn_location():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    location = types.KeyboardButton('Отправить локацию', request_location=True)
    kb.add(location)
    return kb
