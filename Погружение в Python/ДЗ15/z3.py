# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import argparse
from datetime import datetime
from functools import wraps
import logging
from typing import Callable


logging.basicConfig(level=0, filename='D:\GB\ДЗ\Погружение в Python\ДЗ15\log_z3.log', encoding='utf-8', style='{')
logger = logging.getLogger(__name__)

def deco2(func: Callable):
    def wrapper(*args, **kwargs):
        info = {'Аргументы': args}
        result = func(*args, **kwargs)
        info['Результат'] = result
        logger.info(f'{datetime.now()}: {info}')
        return result
    return wrapper


@deco2
def roots_quadratic_equation(a: float, b: float, c:float) -> float | str:
    '''Нахождение корней квадратного уравнения'''
    logger.info(f'уравнение: {a}*x^2+{b}*x+{c}=0')
    print(f'уравнение: {a}*x^2+{b}*x+{c}=0')
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
        x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
        return x1, x2
    elif discriminant == 0:
        x = round(-b / (2 * a), 2)
        return x
    else:
        return 'корней нет'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Решение квадратного уравнения', description='Решение квадратного уравнения с разными коэфициентами', \
                                                                               epilog='квадратное уравнение')
    parser.add_argument('-a', metavar ='a', type = float, default=1)
    parser.add_argument('-b', metavar ='b', type = float, default=0)
    parser.add_argument('-c', metavar ='c', type = float, default=0)
    args = parser.parse_args()
    print(roots_quadratic_equation(args.a, args.b, args.c))