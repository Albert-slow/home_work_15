import telebot
import buttons
import DB
from geopy import Nominatim

bot = telebot.TeleBot(Token)
#  Объект локации
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0')


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    check = DB.check_user(user_id)
    if check:
        bot.send_message(user_id, 'Регистрация прошла успешно!', reply_markup=telebot.types.KeyboardRemove())
    else:
        bot.send_message(user_id, 'Привет'  f'{message.from_user.first_name}, напишите своё имя для регистрации:', reply_markup=telebot.types.ReplyKeyboardRemove)
        bot.register_next_step_handler(message, get_name)


def get_name(message):
        user_id = message.from_user.id
        user_name = message.text
        bot.send_message(user_id, 'Ваше имя успешно зарегистрированно! Теперь введите номер вашего телефона: ', reply_markup=button.btn_num())
        bot.register_next_step_handler(message, get_id, user_name)


def get_number(message):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Номер телефона успешно зарегистрирован! Теперь отправьте локацию: ', reply_markup=button.btn_location())
        bot.register_next_step(message, get_location, user_name, user_number)
    else:
        bot.send_message(user_id, 'Отправьте номер телефона через кнопку!', reply_markup=button.btn_location())
        bot.register_next_step_handler(message, get_number, user_name)


def get_location(message, user_name, user_number):
    user_id = message.from_user.id
    if message.location:
        user_location = geolocator.reverse(f'{message.location.latitude}, {message.location.longitude}')
        DB.register(user_name, user_id, user_number, str(user_location))
        bot.send_message(user_id, 'Регистрация прошла успешно')
    else:
        bot.send_message(user_id, 'Отправьте локацию по кнопке: ', reply_markup=button.btn_location)
        bot.register_next_step_handler(message, get_location, user_name, user_id, user_number)

bot.polling(none_stop=True)

