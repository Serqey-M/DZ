# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions


def noz(x, y):
    if x > y:
        maximum = x
    else:
        maximum = y
    while True:
        if (maximum % x == 0) and (maximum % y == 0):
            noz = maximum
            break
        maximum += 1
    return noz


def nod(x, y):
    if x > y:
        minimum = y
    else:
        minimum = x
    for i in range(minimum, 0, -1):
        if (x % i == 0) and (y % i == 0):
            nod = i
            break
    return nod


fraction_1 = input("Введите первую дробь: ")
fraction_2 = input("Введите вторую дробь: ")

summa = fractions.Fraction(fraction_1) + fractions.Fraction(fraction_2)
multiplication = fractions.Fraction(fraction_1) * fractions.Fraction(fraction_2)
print("fractions")
print(f"{fraction_1} + {fraction_2} = {summa}")
print(f"{fraction_1} * {fraction_2} = {multiplication}")

print("не fractions")
fraction_1_lst = fraction_1.split("/")
fraction_2_lst = fraction_2.split("/")
denominator_sum = noz(int(fraction_1_lst[1]), int(fraction_2_lst[1]))
numerator_sym = int(fraction_1_lst[0]) * denominator_sum / int(fraction_1_lst[1]) + int(
    fraction_2_lst[0]
) * denominator_sum / int(fraction_2_lst[1])
summa_1 = str(int(numerator_sym)) + "/" + str(denominator_sum)
print(f"{fraction_1} + {fraction_2} = {summa_1}")

numerator_mult = int(fraction_1_lst[0]) * int(fraction_2_lst[0])
denominator_mult = int(fraction_1_lst[1]) * int(fraction_2_lst[1])
nod = nod(numerator_mult, denominator_mult)
multiplication = str(int(numerator_mult / nod)) + "/" + str(int(denominator_mult / nod))
print(f"{fraction_1} * {fraction_2} = {multiplication}")
