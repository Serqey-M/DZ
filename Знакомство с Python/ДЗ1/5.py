# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
import os

print("Введите координат х точки A: ")
xA = int(input())
print("Введите координат y точки A: ")
yA = int(input())
print("Введите координат х точки B: ")
xB = int(input())
print("Введите координат y точки B: ")
yB = int(input())
distance = round((math.sqrt(math.pow((xB-xA), 2) + math.pow((yB-yA), 2))), 2)
os.system('CLS')
print(f'A ({xA},{yA}); B ({xB},{yB}) -> {distance}')
