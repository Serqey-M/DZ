# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import os
N = int(input('Введите числj N: '))
while N < 1:
    N = int(input('Введите числj N: '))
list = []
for i in range(2, N+1):
    j = 2
    if i == j:
        list.append(i)
    while i % j != 0:
        j += 1
        if i == j:
            list.append(i)
os.system('CLS')
print(f'Список простых чисел до числа N {list}')

list2 = []
while N > 1:
    for i in list:
        if N % i == 0:
            N /= i
            list2.append(i)

# либо заменить строки 20-23 на строки 26-30
    # i=0
    # while N%list[i]!=0:
    #     i+=1
    # list2.append(list[i])
    # N/=list[i]

print(f'Разложение числа N на простые множители {list2}')


# Разложение числа N на простые множители из интернета

# def primfacs(n):
#    i = 2
#    primfac = []
#    while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n / i
#        i = i + 1
#    if n > 1:
#        primfac.append(n)
#    return primfac
# print(primfacs(100))
