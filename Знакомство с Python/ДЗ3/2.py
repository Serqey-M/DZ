# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
import math
list = []
for i in range (1, random.randint(3, 20)):
    x = random.randint(-100, 100)
    list.append(x)
result = []
for i in range (0, math.ceil(len(list)/2)):
    result.append(list[i]*list[-1-i])
print(f'{list} => {result}')