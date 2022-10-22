# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
k = random.randint(1, 10)
x=0
while x==0:
    coefficients = []
    for i in range(1,k+2):
        coefficients.append(random.randint(0, 100))
    x=0
    i=0
    while i<len(coefficients)-1:
        if coefficients[i] == 0:
            i+=1
        else:
            x=1    
            i+=1        
polynomial=''
x=0
for i in coefficients:
    if k-x == 0:
        if i==0:

            polynomial= polynomial[0:-3] + ' = 0'
        else:
            polynomial= polynomial + str(i) + ' = 0'
    elif k-x == 1:
        if i == 0:
            polynomial= polynomial
        elif i==1:
            polynomial= polynomial + 'x' + " + "    
        else:
            polynomial= polynomial + str(i)+'*x' + " + "
        x+=1
    else:
        if i==0:
            polynomial= polynomial
        elif i==1:
            polynomial= polynomial + 'x^'+ str(k-x)+" + "
        else:
            polynomial= polynomial + str(i)+'*x^'+ str(k-x)+" + "
        x+=1
file = open ('text.txt', 'w')
file.writelines(polynomial)
file.close()
print(polynomial)