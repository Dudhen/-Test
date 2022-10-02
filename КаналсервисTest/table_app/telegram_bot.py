import telebot
from telebot import types
try:
    from table_app.bot_scripts import get_overdue_orders, UserIdList
except ModuleNotFoundError:
    from bot_scripts import get_overdue_orders, UserIdList

bot = telebot.TeleBot("5782497285:AAGFhmTEu5Qj6icAST-CYEJMfjGMEcJa6eQ")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Функция приветственного сообщения ботом,
    а так же отображения кнопки получения списка просроченных номеров заказа
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton("Узнать номера заказов с прошедшим сроком поставки"))
    bot.send_message(message.from_user.id,
                     'Добрый день!\nДобро пожаловать в Каналсервис-бота!\n'
                     'Если вы хотите узнать список номеров с прошедшим сроком поставки - '
                     'нажмите соответствующую кнопку внизу.\n'
                     'Спасибо!\n'
                     'С уважением, Каналсервис-бот!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    """
    Функция ответного сообщения ботом на запрос получения
    списка просроченных номеров заказа
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton("Узнать номера заказов с прошедшим сроком поставки"))
    if message.text == "Узнать номера заказов с прошедшим сроком поставки":
        result = 'Номера заказов с прошедшим сроком поставки:'
        for i_overdue_order in get_overdue_orders():
            for i_key, i_value in i_overdue_order.items():
                result += '\n{}: срок поставки - {}'.format(i_key, i_value)
        if result == 'Номера заказов с прошедшим сроком поставки:':
            result = 'Нет номеров заказа с прошедшим сроком поставки'
    else:
        result = "Прошу прощения, я не понял что вы от меня хотели. Пожалуйста, нажмите кнопку."
    bot.send_message(message.chat.id, text=result, reply_markup=markup)


bot.polling(none_stop=True)