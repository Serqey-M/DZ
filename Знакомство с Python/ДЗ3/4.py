# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import random
number=random.randint(0, 100)
temp_number = number
result = ''
if number==0:
    result='0'
else:
    while temp_number>0:
        result+=str(temp_number%2)  
        temp_number=int(temp_number/2)
print(f'{number} -> {result[::-1]}')