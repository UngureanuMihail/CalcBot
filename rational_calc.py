# модуль для работы с рациональными числами
import math

x = 0
y = 0


# фунцкия для инициализации значении
def init(a, b):
    global x
    global y
    x = a
    y = b

# функция для инициализации одного значения для операций типа sqrt
def init_value(a):
    global x
    x = a


add = lambda: x + y  # сложение значений
diff = lambda: x - y  # вычитание значений
mult = lambda: x * y  # умножение значений
div = lambda: x / y  # деление значений
power = lambda: x ** y  # возведение в степерь значений
