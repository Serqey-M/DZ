# Реализуйте алгоритм перемешивания списка.
import random
from tempfile import tempdir
list = [i for i in range(1,10)]
print(list)
i=0
#while i<len(list):
    #temp_index = random.randint(0, len(list)-1)
    #temp=list[i]
    #list[i]=list[temp_index]
    #list[temp_index]=temp
    #i+=1
for i in range(len(list)):
        # Получение случайного индекса
        index_aleatory = random.randint(0, len(list) - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
print(list)