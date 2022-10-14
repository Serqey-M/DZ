# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму.

n = int(input('Введите число n: '))

dict = {x: round((1 + 1 / x)**x, 2) for x in range(1, n + 1)}
sum = 0
for i in dict:
    sum += dict[i]

print(dict)

print(sum)
print(type(sum))
