# Реализуйте алгоритм перемешивания списка.
import random
from tempfile import tempdir
list = [i for i in range(1, 10)]
print(list)
for i in range(len(list)):
    temp_index = random.randint(0, len(list) - 1)
    temp = list[i]
    list[i] = list[temp_index]
    list[temp_index] = temp
print(list)
