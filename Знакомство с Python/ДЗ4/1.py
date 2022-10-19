# Вычислить число c заданной точностью d (число Пи)
d = float(input('Задайте точность точность. d = '))
n=3
Pi1 = 4
Pi = Pi1-4/n
while abs(Pi-Pi1)>d:
    n+=2
    Pi1=Pi
    Pi=Pi1+4/n
    if abs(Pi-Pi1)>d:
        n+=2
        Pi1=Pi
        Pi=Pi1-4/n
print(Pi)