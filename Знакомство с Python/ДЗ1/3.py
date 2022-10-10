# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

import os
print('Введите координату X отличную от 0:')
X = input()
while X=='0' or X=='':
    print('Введите координату X отличную от 0:')
    X = input()
X=int(X)
print('Введите координату Y отличную от 0:')
Y = input()
while Y=='0' or Y=='':
    print('Введите координату Y отличную от 0:')
    Y = input()
Y=int(Y)
os.system('CLS')
if X>0 and Y>0:
    print(f'X={X}; Y={Y} -> 1')
elif X<0 and Y>0:
    print(f'X={X}; Y={Y} -> 2')
elif X<0 and Y<0:
    print(f'X={X}; Y={Y} -> 3')
else:
    print(f'X={X}; Y={Y} -> 4')