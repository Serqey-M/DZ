# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import os

number = float(input('Введите число: '))
list = []
for i in str(number):
    list.append(i)
list.remove('.')
if list[0] == '-':
    list.remove('-')
sum = 0
for i in list:
    sum += int(i)
os.system('CLS')
print(f'{number} -> {sum}')
