import telebot
import datetime
import math

bot=telebot.TeleBot('5816935308:AAEeJ0UHLqScP90nBMLRA3WVGAx5rov4J3c')
num_1 = 0
num_2 = 0
@bot.message_handler(commands=['menu'])
def menu (message):
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')

@bot.message_handler(commands=['sum'])
def sum (message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message,sum1)
def sum1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message,sum2)
def sum2(message):
    global num_2
    num_2 = message.text
    sum = int(num_1)+int(num_2)
    bot.send_message(message.chat.id, sum)
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: {num_1} + {num_2} = {sum}\n')
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')

@bot.message_handler(commands=['subtracting'])
def subtracting (message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message,subtracting1)
def subtracting1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message,subtracting2)
def subtracting2(message):
    global num_2
    num_2 = message.text
    subtracting = int(num_1)-int(num_2)
    bot.send_message(message.chat.id, subtracting)
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: {num_1} - {num_2} = {subtracting}\n')
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')

@bot.message_handler(commands=['multiply'])
def multiply (message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message,multiply1)
def multiply1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message,multiply2)
def multiply2(message):
    global num_2
    num_2 = message.text
    multiply = int(num_1)*int(num_2)
    bot.send_message(message.chat.id, multiply)
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: {num_1} * {num_2} = {multiply}\n')
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')

@bot.message_handler(commands=['division'])
def division (message):
    bot.send_message(message.chat.id, 'Введите число 1')
    bot.register_next_step_handler(message,division1)
def division1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите число 2')
    bot.register_next_step_handler(message,division2)
def division2(message):
    global num_2
    num_2 = message.text
    division = int(num_1)/int(num_2)
    bot.send_message(message.chat.id, division)
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: {num_1} / {num_2} = {division}\n')  
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')

@bot.message_handler(commands=['exponentiation'])
def exponentiation (message):
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message,exponentiation1)
def exponentiation1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите степень')
    bot.register_next_step_handler(message,exponentiation2)
def exponentiation2(message):
    global num_2
    num_2 = message.text
    exponentiation = math.pow(int(num_1), int(num_2))
    bot.send_message(message.chat.id, exponentiation)
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: {num_1} в степени {num_2} = {exponentiation}\n')    
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')  

@bot.message_handler(commands=['root_extraction'])
def root_extraction (message):
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message,root_extraction1)
def root_extraction1(message):
    global num_1
    num_1 = message.text
    bot.send_message(message.chat.id, 'Введите степень корня')
    bot.register_next_step_handler(message,root_extraction2)
def root_extraction2(message):
    global num_2
    num_2 = message.text
    root_extraction = math.pow(int(num_1), 1/int(num_2))
    bot.send_message(message.chat.id, root_extraction)
    with open('book.txt', 'a', encoding='utf-16') as file:
        file.write(f'{datetime.datetime.now()}: Корень степени {num_2} из числа {num_1} = {root_extraction}\n')
    bot.send_message(message.chat.id, '/sum(+)\n/subtracting(-)\n/multiply(*)\n/division(/)\n/exponentiation(x^y)\n/root_extraction(√)')

bot.polling(none_stop=True, interval=0)