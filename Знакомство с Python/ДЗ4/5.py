# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
def transformation_polynomial(polynomial):
    polynomial = polynomial.replace(' = 0', '')
    polynomial = polynomial.split(' + ')
    for i in range(0, len(polynomial)):
        polynomial[i] = polynomial[i].split('*')
    if len(polynomial[-1]) == 1:
        polynomial[-1].append('x^0')
    for i in range(0, len(polynomial)):
        if len(polynomial[i]) == 1:
            polynomial[i].insert(0, 0)
        polynomial[i][0] = int(polynomial[i][0])
    return polynomial


file = open('text.txt', 'r')
polynomial1 = file.read()
file.close()
print(f'многочлен 1 {polynomial1}')
file = open('text1.txt', 'r')
polynomial2 = file.read()
file.close()
print(f'многочлен 2 {polynomial2}')
polynomial1 = (transformation_polynomial(polynomial1))
polynomial2 = (transformation_polynomial(polynomial2))
sum_polynomial = polynomial1+polynomial2
i = 0
while i < len(sum_polynomial)-1:
    j = i+1
    while j < len(sum_polynomial):
        if sum_polynomial[i][1] == sum_polynomial[j][1]:
            sum_polynomial[i][0] += sum_polynomial[j][0]
            del sum_polynomial[j]
        j += 1
    i += 1
for i in range(0, len(sum_polynomial)):
    sum_polynomial[i][1] = sum_polynomial[i][1].split('^')
    if len(sum_polynomial[i][1]) == 1:
        sum_polynomial[i][1].append('1')
i = 0
while i < len(sum_polynomial):
    j = i+1
    while j < len(sum_polynomial):
        if (int(sum_polynomial[i][1][1]) < int(sum_polynomial[j][1][1])):
            sum_polynomial.insert(i, sum_polynomial[j])
            del sum_polynomial[j+1]
        j += 1
    i += 1
for i in range(0, len(sum_polynomial)):
    if sum_polynomial[i][1][1] == '1':
        sum_polynomial[i][1].pop()
    sum_polynomial[i][1] = "^".join(sum_polynomial[i][1])
    if sum_polynomial[i][1] == 'x^0':
        sum_polynomial[i].pop()
    sum_polynomial[i][0] = str(sum_polynomial[i][0])
    if sum_polynomial[i][0] == '0':
        sum_polynomial[i].pop(0)
    sum_polynomial[i] = "*".join(sum_polynomial[i])
sum_polynomial = " + ".join(sum_polynomial)+' = 0'
print(sum_polynomial)
