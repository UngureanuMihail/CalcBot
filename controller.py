import math
import logger
import rational_calc
import complexmath


def button_add(value_x, value_y):
    rational_calc.init(value_x, value_y)
    result = rational_calc.add()
    return result


def button_diff(value_x, value_y):
    rational_calc.init(value_x, value_y)
    result = rational_calc.diff()
    return result


def button_mult(value_x, value_y):
    rational_calc.init(value_x, value_y)
    result = rational_calc.mult()
    return result


def button_div(value_x, value_y):
    result = complexmath.div(value_x, value_y)
    return result


def button_power(value_x, value_y):
    rational_calc.init(value_x, value_y)
    result = rational_calc.power()
    return result


def button_sqrt(value_x):
    result = complexmath.sqrt(value_x)
    return result


# # метод для вывода меню
# def menu():
#     global message
#     message = ('Для сложения введите "+"\n'
#                'Для вычитание введите "-"\n'
#                'Для умножение введите "*"\n'
#                'Для деление введите "/"\n'
#                'Для извлечения корня введите "sqrt"\n'
#                'Для возведение в степерь введите "^"')
#     print(message)


def run(choice, value_x, value_y):
    result = 0
    comand_dict = {'+': button_add,
                   '-': button_diff,
                   '*': button_mult,
                   '/': button_div,
                   '^': button_power,
                   '√': button_sqrt}
    if choice in comand_dict:
        if choice != '√':
            result = comand_dict[choice](value_x, value_y)
        else:
            result = comand_dict[choice](value_x)
    return result
