# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число.
import random
lst = [random.randint(-10, 10) for a in range(10)]
print(f'список {lst}')
num = random.randint(-10, 10)
if True in map(lambda x: x == num, lst):
    print(f'число {num} -> да')
else:
    print (f'число {num} -> нет')
