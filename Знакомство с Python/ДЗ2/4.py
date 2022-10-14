# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
import os
N = int(input('Введите значение N: '))
list = [random.randint(-N, N) for a in range(N)]
file = open('file.txt', 'r')
positions = [int(line) for line in file]
file.close()
result = 1
list1 = []
i = 0
while i < len(positions):
    result *= list[positions[i]-1]
    print(list[positions[i]-1])
    i += 1
os.system('CLS')
print(f'список: {list}')
print(f'позиции: {positions}')
print(f'результат: {result}')
