# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import os
print('Введите номер четверти:')
X = input()
while X!='1' and X!='2'and X!='3'and X!='4':
    print('Введите номер четверти:')
    X = input()
os.system('CLS')
if X=='1':
    print('1 четверть: X > 0; Y > 0')
elif X=='2':
    print('2 четверть: X < 0; Y > 0')
elif X=='3':
    print('3 четверть: X < 0; Y < 0')
else:
    print('4 четверть: X > 0; Y < 0')