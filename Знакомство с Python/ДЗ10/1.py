# Создать калькулятор для работы с рациональными и (*)комплексными числами, организовать меню, добавив в неё систему логирования

import telebot
import datetime

bot = telebot.TeleBot('5816935308:AAEeJ0UHLqScP90nBMLRA3WVGAx5rov4J3c')
num_1 = 0
num_2 = 0
complex_num_1 = []
complex_num_2 = []


@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['rational_numbers'])
def rational_numbers(message):
    bot.send_message(
        message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')


@bot.message_handler(commands=['sum'])
def sum(message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message, sum1)


def sum1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message, sum2)


def sum2(message):
    global num_2
    num_2 = message.text
    sum = float(num_1)+float(num_2)
    bot.send_message(message.chat.id, f'{num_1} + {num_2} = {sum}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: {num_1} + {num_2} = {sum}\n')
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['subtracting'])
def subtracting(message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message, subtracting1)


def subtracting1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message, subtracting2)


def subtracting2(message):
    global num_2
    num_2 = message.text
    subtracting = float(num_1)-float(num_2)
    bot.send_message(message.chat.id, f'{num_1} - {num_2} = {subtracting}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {num_1} - {num_2} = {subtracting}\n')
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['multiply'])
def multiply(message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message, multiply1)


def multiply1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message, multiply2)


def multiply2(message):
    global num_2
    num_2 = message.text
    multiply = float(num_1)*float(num_2)
    bot.send_message(message.chat.id, f'{num_1} * {num_2} = {multiply}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {num_1} * {num_2} = {multiply}\n')
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['division'])
def division(message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message, division1)


def division1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message, division2)


def division2(message):
    global num_2
    num_2 = message.text
    division = float(num_1)/float(num_2)
    bot.send_message(message.chat.id, f'{num_1} / {num_2} = {division}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {num_1} / {num_2} = {division}\n')
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['exponentiation'])
def exponentiation(message):
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message, exponentiation1)


def exponentiation1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите степень')
    bot.register_next_step_handler(message, exponentiation2)


def exponentiation2(message):
    global num_2
    num_2 = message.text
    exponentiation = pow(float(num_1), float(num_2))
    bot.send_message(
        message.chat.id, f'{num_1} в степени {num_2} = {exponentiation}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {num_1} в степени {num_2} = {exponentiation}\n')
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['root_extraction'])
def root_extraction(message):
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message, root_extraction1)


def root_extraction1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите степень корня')
    bot.register_next_step_handler(message, root_extraction2)


def root_extraction2(message):
    global num_2
    num_2 = message.text
    root_extraction = pow(float(num_1), 1/float(num_2))
    bot.send_message(
        message.chat.id, f'Корень степени {num_2} из числа {num_1} = {root_extraction}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: Корень степени {num_2} из числа {num_1} = {root_extraction}\n')
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['complex_numbers'])
def complex_numbers(message):
    bot.send_message(
        message.chat.id, '/complex_sum(+)\n/complex_subtracting(-)\n/complex_multiply(*)\n/complex_division(/)\n/complex_exponentiation(x^y)\n/complex_root_extraction(√)')


@bot.message_handler(commands=['complex_sum'])
def complex_sum(message):
    bot.send_message(message.chat.id, 'Введите действительную часть числа 1')
    bot.register_next_step_handler(message, complex_sum_d1)


def complex_sum_d1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 1')
    bot.register_next_step_handler(message, complex_sum_m1)


def complex_sum_m1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите действительную часть числа 2')
    bot.register_next_step_handler(message, complex_sum_d2)


def complex_sum_d2(message):
    global complex_num_2
    complex_num_2.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 2')
    bot.register_next_step_handler(message, complex_sum_m2)


def complex_sum_m2(message):
    global complex_num_2
    global complex_num_1
    complex_num_2.append(float(message.text))
    complex_num_1 = complex(complex_num_1[0], complex_num_1[1])
    complex_num_2 = complex(complex_num_2[0], complex_num_2[1])
    complex_sum = complex_num_1+complex_num_2
    bot.send_message(
        message.chat.id, f'{complex_num_1} + {complex_num_2} = {complex_sum}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {complex_num_1} + {complex_num_2} = {complex_sum}\n')
    complex_num_1 = []
    complex_num_2 = []
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['complex_subtracting'])
def complex_subtracting(message):
    bot.send_message(message.chat.id, 'Введите действительную часть числа 1')
    bot.register_next_step_handler(message, complex_subtracting_d1)


def complex_subtracting_d1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 1')
    bot.register_next_step_handler(message, complex_subtracting_m1)


def complex_subtracting_m1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите действительную часть числа 2')
    bot.register_next_step_handler(message, complex_subtracting_d2)


def complex_subtracting_d2(message):
    global complex_num_2
    complex_num_2.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 2')
    bot.register_next_step_handler(message, complex_subtracting_m2)


def complex_subtracting_m2(message):
    global complex_num_2
    global complex_num_1
    complex_num_2.append(float(message.text))
    complex_num_1 = complex(complex_num_1[0], complex_num_1[1])
    complex_num_2 = complex(complex_num_2[0], complex_num_2[1])
    complex_subtracting = complex_num_1-complex_num_2
    bot.send_message(
        message.chat.id, f'{complex_num_1} - {complex_num_2} = {complex_subtracting}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {complex_num_1} - {complex_num_2} = {complex_subtracting}\n')
    complex_num_1 = []
    complex_num_2 = []
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['complex_multiply'])
def complex_multiply(message):
    bot.send_message(message.chat.id, 'Введите действительную часть числа 1')
    bot.register_next_step_handler(message, complex_multiply_d1)


def complex_multiply_d1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 1')
    bot.register_next_step_handler(message, complex_multiply_m1)


def complex_multiply_m1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите действительную часть числа 2')
    bot.register_next_step_handler(message, complex_multiply_d2)


def complex_multiply_d2(message):
    global complex_num_2
    complex_num_2.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 2')
    bot.register_next_step_handler(message, complex_multiply_m2)


def complex_multiply_m2(message):
    global complex_num_2
    global complex_num_1
    complex_num_2.append(float(message.text))
    complex_num_1 = complex(complex_num_1[0], complex_num_1[1])
    complex_num_2 = complex(complex_num_2[0], complex_num_2[1])
    complex_multiply = complex_num_1*complex_num_2
    bot.send_message(
        message.chat.id, f'{complex_num_1} * {complex_num_2} = {complex_multiply}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {complex_num_1} * {complex_num_2} = {complex_multiply}\n')
    complex_num_1 = []
    complex_num_2 = []
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['complex_division'])
def complex_division(message):
    bot.send_message(message.chat.id, 'Введите действительную часть числа 1')
    bot.register_next_step_handler(message, complex_division_d1)


def complex_division_d1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 1')
    bot.register_next_step_handler(message, complex_division_m1)


def complex_division_m1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите действительную часть числа 2')
    bot.register_next_step_handler(message, complex_division_d2)


def complex_division_d2(message):
    global complex_num_2
    complex_num_2.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа 2')
    bot.register_next_step_handler(message, complex_division_m2)


def complex_division_m2(message):
    global complex_num_2
    global complex_num_1
    complex_num_2.append(float(message.text))
    complex_num_1 = complex(complex_num_1[0], complex_num_1[1])
    complex_num_2 = complex(complex_num_2[0], complex_num_2[1])
    complex_division = complex_num_1/complex_num_2
    bot.send_message(
        message.chat.id, f'{complex_num_1} / {complex_num_2} = {complex_division}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {complex_num_1} / {complex_num_2} = {complex_division}\n')
    complex_num_1 = []
    complex_num_2 = []
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['complex_exponentiation'])
def complex_exponentiation(message):
    bot.send_message(message.chat.id, 'Введите действительную часть числа')
    bot.register_next_step_handler(message, complex_exponentiation_d1)


def complex_exponentiation_d1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа')
    bot.register_next_step_handler(message, complex_exponentiation_m1)


def complex_exponentiation_m1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите степень')
    bot.register_next_step_handler(message, complex_exponentiation_m2)


def complex_exponentiation_m2(message):
    global complex_num_1
    Pow = float(message.text)
    complex_num_1 = complex(complex_num_1[0], complex_num_1[1])
    complex_exponentiation = pow(complex_num_1, Pow)
    bot.send_message(
        message.chat.id, f'{complex_num_1} в степени {Pow} = {complex_exponentiation}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: {complex_num_1} в степени {Pow} = {complex_exponentiation}\n')
    complex_num_1 = []
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


@bot.message_handler(commands=['complex_root_extraction'])
def complex_root_extraction(message):
    bot.send_message(message.chat.id, 'Введите действительную часть числа')
    bot.register_next_step_handler(message, complex_root_extraction_d1)


def complex_root_extraction_d1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите мниммую частью числа')
    bot.register_next_step_handler(message, complex_root_extraction_m1)


def complex_root_extraction_m1(message):
    global complex_num_1
    complex_num_1.append(float(message.text))
    bot.send_message(message.chat.id, 'Введите степень корня')
    bot.register_next_step_handler(message, complex_root_extraction_m2)


def complex_root_extraction_m2(message):
    global complex_num_1
    Pow = float(message.text)
    complex_num_1 = complex(complex_num_1[0], complex_num_1[1])
    complex_root_extraction = pow(complex_num_1, 1/Pow)
    bot.send_message(
        message.chat.id, f'корень степени {Pow} из числа {complex_num_1} = {complex_root_extraction}')
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(
            f'{datetime.datetime.now()}: корень степени {Pow} из числа {complex_num_1} = {complex_root_extraction}\n')
    complex_num_1 = []
    bot.send_message(message.chat.id, '/rational_numbers\n/complex_numbers')


bot.polling(none_stop=True, interval=0)
