# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random
import os
print('Условия игры')
initial_quantity = int(input('Введите начальное количество конфет: '))
max_step = int(
    input('Введите какое количество конфет можно взять за один ход: '))
while initial_quantity > 0:
    os.system('CLS')
    print(f'Осталось конфет: {initial_quantity}')
    player_1 = int(input(f'ход игрока 1 (1-{max_step}):'))
    while player_1 < 1 or player_1 > max_step:
        player_1 = int(
            input(f'не допустимое значение, ход игрока 1 (1-{max_step}): '))
    initial_quantity -= player_1
    if initial_quantity < 1:
        print('Игрок 1 победил')
    else:
        os.system('CLS')
        print(f'Осталось конфет: {initial_quantity}')
        player_2 = int(input(f'ход игрока 2 (1-{max_step}):'))
        while player_2 < 1 or player_2 > max_step:
            player_2 = int(
                input(f'не допустимое значение, ход игрока 2 (1-{max_step}): '))
        initial_quantity -= player_2
        if initial_quantity < 1:
            print('Игрок 2 победил')