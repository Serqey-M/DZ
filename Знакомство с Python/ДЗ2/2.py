# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import os

N = int(input('Введите положительное число: '))
while N < 1:
    N = int(input('Введите положительное число: '))
list = [1]
i = 2
while i <= N:
    list.append(i*list[i-2])
    i += 1
os.system('CLS')
print(f'N = {N} результат {list}')
