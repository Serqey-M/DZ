# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
import random
k = random.randint(1, 10)
Fibonacci = [0]*(k*2+1)
Fibonacci[k] = 0
Fibonacci[k+1] = 1
Fibonacci[k-1] = 1
x = 2
for i in range(k+2, k*2+1):
    Fibonacci[i] = Fibonacci[i-1]+Fibonacci[i-2]
    Fibonacci[k-x] = Fibonacci[k-x+2]-Fibonacci[k-x+1]
    x += 1
print(f'для k = {k} список будет выглядеть так: {Fibonacci}')
