# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True, 
# если команда успешно выполнена и текст найден в её выводе и False в противном случае. Передаваться должна только одна строка, 
# разбиение вывода использовать не нужно.
# Задание 2. (повышенной сложности)
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, 
# в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). 
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
from string import punctuation


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if result.returncode == 0 and text in result.stdout:
        print(type(result.stdout))
        return True
    else:
        return False


def checkout1(cmd, text, mode=0):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    res = False
    if result.returncode == 0:
        match mode:
            case 0:
                if text in result.stdout:
                    res = True
            case 1:
                for i in punctuation:
                    result.stdout = result.stdout.replace(i, '')
                if text in result.stdout:
                    res = True
            case _:
                res = 'Недопустимое значение mode'
    return res