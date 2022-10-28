# Создайте программу для игры в ""Крестики-нолики"".

import os


game_field = {'X0': ' ', 'X1': '1', 'X2': '2', 'X3': '3',
              'A0': 'A', 'A1': '-', 'A2': '-', 'A3': '-',
              'B0': 'B', 'B1': '-', 'B2': '-', 'B3': '-',
              'C0': 'C', 'C1': '-', 'C2': '-', 'C3': '-'}

print(game_field['X0'] + '  ' + game_field['X1'] +
      '  ' + game_field['X2']+'  ' + game_field['X3'])
print(game_field['A0'] + '  ' + game_field['A1'] +
      '  ' + game_field['A2']+'  ' + game_field['A3'])
print(game_field['B0'] + '  ' + game_field['B1'] +
      '  ' + game_field['B2']+'  ' + game_field['B3'])
print(game_field['C0'] + '  ' + game_field['C1'] +
      '  ' + game_field['C2']+'  ' + game_field['C3'])

i = 0
while i < 9:
    step1 = input('Ход игрока 1(пример - А1): ')
    while step1 != 'A1' and step1 != 'A2' and step1 != 'A3' and \
            step1 != 'B1' and step1 != 'B2' and step1 != 'B3' and \
            step1 != 'C1' and step1 != 'C1' and step1 != 'C1':
        step1 = input('Недопустимое значение. Ход игрока 1 (пример - А1): ')
    else:
        while game_field[step1] != '-':
            step1 = input('Ячейка занята. Ход игрока 1 (пример - А1): ')
        else:
            game_field[step1] = 'X'
    os.system('CLS')
    print(game_field['X0'] + '  ' + game_field['X1'] +
          '  ' + game_field['X2']+'  ' + game_field['X3'])
    print(game_field['A0'] + '  ' + game_field['A1'] +
          '  ' + game_field['A2']+'  ' + game_field['A3'])
    print(game_field['B0'] + '  ' + game_field['B1'] +
          '  ' + game_field['B2']+'  ' + game_field['B3'])
    print(game_field['C0'] + '  ' + game_field['C1'] +
          '  ' + game_field['C2']+'  ' + game_field['C3'])
    if game_field['A1'] == game_field['A2'] == game_field['A3'] == 'X' or\
       game_field['B1'] == game_field['B2'] == game_field['B3'] == 'X' or\
       game_field['C1'] == game_field['C2'] == game_field['C3'] == 'X' or\
       game_field['A1'] == game_field['B1'] == game_field['C1'] == 'X' or\
       game_field['A2'] == game_field['B2'] == game_field['C2'] == 'X' or\
       game_field['A3'] == game_field['B3'] == game_field['C3'] == 'X' or\
       game_field['A1'] == game_field['B2'] == game_field['C3'] == 'X' or\
       game_field['C1'] == game_field['B2'] == game_field['A3'] == 'X':
        print('Игрок 1 победил')
        exit()
    i += 1
    if i == 9:
        print('Ничья')
        exit()
    step2 = input('Ход игрока 2(пример - А1): ')
    while step2 != 'A1' and step2 != 'A2' and step2 != 'A3' and \
            step2 != 'B1' and step2 != 'B2' and step2 != 'B3' and \
            step2 != 'C1' and step2 != 'C1' and step2 != 'C1':
        step2 = input('Недопустимое значение. Ход игрока 2 (пример - А1): ')
    else:
        while game_field[step2] != '-':
            step2 = input('Ячейка занята. Ход игрока 2 (пример - А1): ')
        else:
            game_field[step2] = 'O'
    os.system('CLS')
    print(game_field['X0'] + '  ' + game_field['X1'] +
          '  ' + game_field['X2']+'  ' + game_field['X3'])
    print(game_field['A0'] + '  ' + game_field['A1'] +
          '  ' + game_field['A2']+'  ' + game_field['A3'])
    print(game_field['B0'] + '  ' + game_field['B1'] +
          '  ' + game_field['B2']+'  ' + game_field['B3'])
    print(game_field['C0'] + '  ' + game_field['C1'] +
          '  ' + game_field['C2']+'  ' + game_field['C3'])
    if game_field['A1'] == game_field['A2'] == game_field['A3'] == 'O' or\
       game_field['B1'] == game_field['B2'] == game_field['B3'] == 'O' or\
       game_field['C1'] == game_field['C2'] == game_field['C3'] == 'O' or\
       game_field['A1'] == game_field['B1'] == game_field['C1'] == 'O' or\
       game_field['A2'] == game_field['B2'] == game_field['C2'] == 'O' or\
       game_field['A3'] == game_field['B3'] == game_field['C3'] == 'O' or\
       game_field['A1'] == game_field['B2'] == game_field['C3'] == 'O' or\
       game_field['C1'] == game_field['B2'] == game_field['A3'] == 'O':
        print('Игрок 2 победил')
        exit()
    i += 1
