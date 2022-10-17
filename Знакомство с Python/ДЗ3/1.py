# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции (по индексу).
import random
import os
list = []
for i in range (1, random.randint(3, 20)):
    x = random.randint(-100, 100)
    list.append(x)
sum=list[1]
elements = 'на нечетных позициях элементы:'+ str(list[1])+','
for i in range(3,len(list),2):
    sum+=list[i]
    elements+= str(list[i])+','
os.system('CLS')
print(f'{list} -> {elements} ответ: {sum}')