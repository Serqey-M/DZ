# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import csv
from functools import wraps
import json
import random
from typing import Callable


def generation_csv_file(directory: str, min_num: float = -100, max_num: float = 100, num_rows: int = 100) -> None:
    all_data = []
    for _ in range(num_rows):
        all_data.append((round(random.uniform(min_num, max_num), 2), round(random.uniform(min_num, max_num), 2), round(random.uniform(min_num, max_num), 2)))
    with open(f'{directory}\\file.csv', 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f, dialect='excel-tab')
        csv_write.writerows(all_data)


def deco_1(directory: str):
    def deco1(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dct ={}
            with open(f'{directory}\\file.csv', 'r', encoding='utf-8') as file:
                csv_file = csv.reader(file, dialect='excel-tab', quoting = csv.QUOTE_NONNUMERIC)
                for i, line in enumerate(csv_file):
                    args = (line[0], line[1], line[2])
                    result = func(*args, **kwargs)
                    dct[f'уравнение {i}'] = {'параметры': args, 'корни': result}
                    print(f'корни уравнения: {result}')
            return dct
        return wrapper
    return deco1


def deco_2(directory: str):
    def deco2(func: Callable):
        @wraps(func)    
        def wrapper(*args):
            result = func(*args)
            with open(f'{directory}\\file.json', 'w+', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2) 
            return result
        return wrapper
    return deco2


@deco_2('D:\GB\ДЗ\Погружение в Python\ДЗ9')
@deco_1('D:\GB\ДЗ\Погружение в Python\ДЗ9')
def roots_quadratic_equation(a: float, b: float, c:float) -> float | str:
    '''Нахождение корней квадратного уравнения'''
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
    generation_csv_file('D:\GB\ДЗ\Погружение в Python\ДЗ9')
    roots_quadratic_equation()
    help(roots_quadratic_equation)