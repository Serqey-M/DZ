# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
def transformation_polynomial (polynomial):
    polynomial = polynomial.replace(' = 0', '')
    polynomial = polynomial.split(' + ')
    for i in range(0, len(polynomial)):
        polynomial[i]=polynomial[i].split('*')
        polynomial[i][0]= int(polynomial[i][0])
    if len(polynomial[-1])==1:
        polynomial[-1].append('!')
    return polynomial

file = open ('text.txt', 'r')
polynomial1= file.read()
file.close()
print (f'многочлен 1 {polynomial1}')
file = open ('text1.txt', 'r')
polynomial2= file.read()
file.close()
print(f'многочлен 2 {polynomial2}')
polynomial1= (transformation_polynomial(polynomial1))
polynomial2= (transformation_polynomial(polynomial2))

if len(polynomial1)>len(polynomial2):
    sum_polynomial=polynomial1.copy()
    for i in range(0, len(sum_polynomial)-1):
        for j in range(0, len(polynomial2)):
            if sum_polynomial[i][1] == polynomial2[j][1]:
                sum_polynomial[i][0]+=polynomial2[j][0]
else:
    sum_polynomial=polynomial2.copy()
    for i in range(0, len(sum_polynomial)):
        for j in range(0, len(polynomial1)):
            if sum_polynomial[i][1] == polynomial1[j][1]:
                sum_polynomial[i][0]+= polynomial1[j][0]
            






print(sum_polynomial)
