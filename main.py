from telebot import types
import telebot
from decimal import Decimal
from logger import log
from Settings import TOKEN
from controller import run

bot = telebot.TeleBot(TOKEN, parse_mode=None)
operations = ['+', '-', '*', '/', '^', '√']
user_variables_dict = dict()


@bot.message_handler(commands=['start'])
def start(message):
    user_markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name} '
                                           f'для работы с рациональными числами воспользуйтесь комнадой /rational,'
                                           f' а для комплексных чисел командой /complex.\n Данные команды можно найти'
                                           f' в меню быстрого доступа', reply_markup=user_markup)


@bot.message_handler(commands=['rational', 'complex'])
def calc_start(message):
    user_markup = types.ReplyKeyboardRemove(selective=False)
    user_variables_dict[message.from_user.id] = [Decimal(0), '', Decimal(0), False]
    if message.text == '/complex':
        user_variables_dict[message.from_user.id][3] = True
        print(user_variables_dict)
    msg = bot.send_message(message.from_user.id, 'Введите первое число', reply_markup=user_markup)
    bot.register_next_step_handler(msg, first_step)


def first_step(message):
    flag = user_variables_dict[message.from_user.id][3]
    try:
        if flag:
            user_variables_dict[message.from_user.id][0] = complex(message.text)
        else:
            user_variables_dict[message.from_user.id][0] = Decimal(message.text)
    except:
        mesg = 'Некорректный ввод'
        if flag:
            mesg += 'Формат ввода комплексных чисел: 2+5j'
        log(message.from_user.id, mesg)
        bot.send_message(message.from_user.id, mesg)
        return
    user_markup = types.ReplyKeyboardMarkup(True, False)
    for i in range(len(operations) // 3):
        user_markup.row(*operations[3 * i:3 * (i + 1)])
    msg = bot.send_message(message.from_user.id, 'Выберите операцию', reply_markup=user_markup)
    bot.register_next_step_handler(msg, second_step)


def second_step(message):
    inpt = message.text
    user_markup = types.ReplyKeyboardRemove(selective=False)
    if inpt in operations:
        user_variables_dict[message.from_user.id][1] = inpt
    else:
        log(message.from_user.id, 'Некорректный операция')
        bot.send_message(message.from_user.id, 'Некорректный операция', reply_markup=user_markup)
        return

    if user_variables_dict[message.from_user.id][1] == '√':
        num1, action, num2 = user_variables_dict[message.from_user.id][:3]
        result = f'{action}{str(num1)} = {run(action, num1, num2)}'
        log(message.from_user.id, result)
        bot.send_message(message.from_user.id, result, reply_markup=user_markup)
    else:
        msg = bot.send_message(message.from_user.id, 'Введите второе число', reply_markup=user_markup)
        bot.register_next_step_handler(msg, calc_result)


def calc_result(message):
    flag = user_variables_dict[message.from_user.id][3]
    try:
        if flag:
            user_variables_dict[message.from_user.id][2] = complex(message.text)
        else:
            user_variables_dict[message.from_user.id][2] = Decimal(message.text)
    except:
        mesg = 'Некорректный ввод'
        if flag:
            mesg += 'Формат ввода комплексных чисел: 2+5j'
        log(message.from_user.id, mesg)
        bot.send_message(message.from_user.id, mesg)
        return
    num1, action, num2 = user_variables_dict[message.from_user.id][:3]
    user_markup = types.ReplyKeyboardMarkup(True, False)
    result = f'{str(num1)} {action} {str(num2)} = {run(action, num1, num2)}'
    log(message.from_user.id, result)
    bot.send_message(message.from_user.id, result, reply_markup=user_markup)


print('start')

bot.infinity_polling()
