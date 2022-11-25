import file_list
import print1


def sorting():
    print('\nПо какому признаку отсортировать?\n')
    print('1. Фамилия.\n2. Имя.\n3. Отчество.\n4. Отдел.\n5. Должность.\n6. Номер телефона 1.')
    x = int(input())-1
    lst = file_list.lst()
    lst = list(map(lambda i: i.split(', '), lst))
    for i in range(len(lst)):
        lst[i] = list(map(lambda i: i.split(': '), lst[i]))
    for i in range(len(lst)):
        min = lst[i][x][1]
        z = i
        for j in range(i, len(lst)-i):
            if lst[j][x][1] < min:
                min = lst[j][x][1]
                z = j
        temp = lst[i]
        lst[i] = lst[z]
        lst[z] = temp
    for i in range(len(lst)):
        lst[i] = map(lambda i: ': '.join(i), lst[i])
    lst = map(lambda i: ', '.join(i), lst)
    with open('employees.csv', 'w', encoding="utf-8") as data:
        data.writelines(lst)
    print1.print_all_to_console()
