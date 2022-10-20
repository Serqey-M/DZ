# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
list = []
for i in range(1, random.randint(10, 20)):
    x = random.randint(0, 10)
    list.append(x)
list1 = [list[0]]
for i in list:
    x = 0
    for j in list1:
        if j != i and x == 0:
            x = 0
        else:
            x = 1
    if x == 0:
        list1.append(i)
print(list)
print(list1)
