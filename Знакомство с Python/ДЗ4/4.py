# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
k = random.randint(1, 10)
coefficients = []
for i in range(1,k+2):
    coefficients.append(random.randint(0, 100))
polynomial=''
x=0
for i in coefficients:
    if k-x == 0:
        polynomial= polynomial + str(i) + ' = 0'
    elif k-x == 1:
        polynomial= polynomial + str(i)+'*x' + " + "
        x+=1
    else:
        polynomial= polynomial + str(i)+'*x^'+ str(k-x)+" + "
        x+=1
file = open ('text.txt', 'w')
file.writelines(polynomial)
file.close()
print(polynomial)