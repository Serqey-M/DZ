# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# step_player:
# step = int(input(f'ход игрока (1-{max_step}): '))
# while step < 1 or step > max_step:
# step = int(input(f'не допустимое значение, ход игрока (1-{max_step}): '))
    

import random
import os
print('Условия игры')
initial_quantity = int(input('Введите начальное количество конфет: '))
max_step = int(input('Введите какое количество конфет можно взять за один ход: '))
toss = (random.randint(0,1))
while initial_quantity > 0:
    os.system('CLS')
    if toss == 0:
        print(f'Осталось конфет: {initial_quantity}')
        step_player = int(input(f'ход игрока (1-{max_step}):'))
        while step_player < 1 or step_player > max_step:
            player_1 = int(input(f'не допустимое значение, ход игрока (1-{max_step}): '))
        initial_quantity -= step_player
        toss = 1
        if initial_quantity < 1:
            print('Игрок подедил')
    else:
        step_bot = (random.randint(1,max_step))
        initial_quantity -= step_bot
        if initial_quantity < 1:
            print('Бот победил')