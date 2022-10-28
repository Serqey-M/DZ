# Создайте программу для игры в ""Крестики-нолики"".

from ast import While


game_field = {'X0':' ','X1':'1','X2':'2','X3':'3',\
              'A0':'A','A1':'-','A2':'-','A3':'-',\
              'B0':'B','B1':'-','B2':'-','B3':'-',\
              'C0':'C','C1':'-','C2':'-','C3':'-'}

print(game_field['X0'] + '  ' + game_field['X1']+'  ' + game_field['X2']+'  ' +game_field['X3'])
print(game_field['A0'] +'  ' + game_field['A1']+ '  ' +game_field['A2']+'  ' +game_field['A3'])
print(game_field['B0'] +'  ' + game_field['B1']+'  ' + game_field['B2']+'  ' +game_field['B3'])
print(game_field['C0'] +'  ' + game_field['C1']+'  ' +game_field['C2']+'  ' +game_field['C3'])

i=0
while i<9:
    step1 = input('Ход игрока 1(пример - А1): ' )
    game_field[step1] = 'X'
    print(game_field['X0'] + '  ' + game_field['X1']+'  ' + game_field['X2']+'  ' +game_field['X3'])
    print(game_field['A0'] +'  ' + game_field['A1']+ '  ' +game_field['A2']+'  ' +game_field['A3'])
    print(game_field['B0'] +'  ' + game_field['B1']+'  ' + game_field['B2']+'  ' +game_field['B3'])
    print(game_field['C0'] +'  ' + game_field['C1']+'  ' +game_field['C2']+'  ' +game_field['C3'])
    if game_field['A1']==game_field['A2']==game_field['A3']=='X' or\
       game_field['B1']==game_field['B2']==game_field['B3']=='X' or\
       game_field['C1']==game_field['C2']==game_field['C3']=='X' or\
       game_field['A1']==game_field['B1']==game_field['C1']=='X' or\
       game_field['A2']==game_field['B2']==game_field['C2']=='X' or\
       game_field['A3']==game_field['B3']==game_field['C3']=='X' or\
       game_field['A1']==game_field['B2']==game_field['C3']=='X' or\
       game_field['C1']==game_field['B2']==game_field['A3']=='X':
       print('Игрок 1 победил')
       exit() 
    i+=1
    if i==9:
        print('Ничья')
        exit()
    
    step2 = input('Ход игрока 2(пример - А1): ')
    game_field[step2] = 'O'
    print(game_field['X0'] + '  ' + game_field['X1']+'  ' + game_field['X2']+'  ' +game_field['X3'])
    print(game_field['A0'] +'  ' + game_field['A1']+ '  ' +game_field['A2']+'  ' +game_field['A3'])
    print(game_field['B0'] +'  ' + game_field['B1']+'  ' + game_field['B2']+'  ' +game_field['B3'])
    print(game_field['C0'] +'  ' + game_field['C1']+'  ' +game_field['C2']+'  ' +game_field['C3'])
    if game_field['A1']==game_field['A2']==game_field['A3']=='O' or\
       game_field['B1']==game_field['B2']==game_field['B3']=='O' or\
       game_field['C1']==game_field['C2']==game_field['C3']=='O' or\
       game_field['A1']==game_field['B1']==game_field['C1']=='O' or\
       game_field['A2']==game_field['B2']==game_field['C2']=='O' or\
       game_field['A3']==game_field['B3']==game_field['C3']=='O' or\
       game_field['A1']==game_field['B2']==game_field['C3']=='O' or\
       game_field['C1']==game_field['B2']==game_field['A3']=='O':
       print('Игрок 2 победил')
       exit()
    i+=1