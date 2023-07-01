# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

REPRESENTATION = 16

number_10 = int(input("Ввдете целое число: "))
print(hex(number_10))
number_16 = ""

while number_10 != 0:
    remainder = number_10 % REPRESENTATION
    number_10 = number_10 // REPRESENTATION
    match remainder:
        case 10:
            number_16 = "a" + number_16
        case 11:
            number_16 = "b" + number_16
        case 12:
            number_16 = "c" + number_16
        case 13:
            number_16 = "d" + number_16
        case 14:
            number_16 = "e" + number_16
        case 15:
            number_16 = "f" + number_16
        case _:
            number_16 = str(remainder) + number_16
print(number_16)
