# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
number_rows = int(input("Введите количество рядов: "))
for i in range(1, number_rows+1):
    print(f"{' '*(number_rows-i)}{'*'*(2*i-1)}")