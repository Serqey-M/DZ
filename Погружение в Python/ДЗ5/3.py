# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def Fibonacci(num):
    Fibonacci = [0, 1]
    for _ in range(2, num):
        Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
    return Fibonacci


if __name__ == '__main__':
    print(Fibonacci(10))