# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
list = []
for i in range(1, random.randint(3, 20)):
    x = round(random.uniform(-100.99, 100.99), 2)
    list.append(x)
fractional_part = []
for i in range(0, len(list)):
    fractional_part.append(abs(round(list[i]-int(list[i]), 2)))
max = fractional_part[i]
min = fractional_part[i]
for i in fractional_part:
    if i > max:
        max = i
    elif i < min:
        min = i
print(f'{list} => {round((max-min),2)}')
