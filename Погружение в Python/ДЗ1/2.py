# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2,10):
    for j in range(2,6):
        multiplication = i*j
        if multiplication>9:
            print(f'{j} x {i} = {multiplication}', end='   ') 
        else:
            print(f'{j} x {i} =  {multiplication}', end='   ')
    print("")
print("")
for i in range(2,10):
    for j in range(6,10):
        multiplication = i*j
        if multiplication>9:
            print(f'{j} x {i} = {multiplication}', end='   ') 
        else:
            print(f'{j} x {i} =  {multiplication}', end='   ')
    print("")    