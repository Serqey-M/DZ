import print1
import file_list


def Edit_Entry():
    print1.print_all_to_console()
    lst = file_list.lst()
    z = int(input('Какую строку необходимо изменить? '))
    lst[z-1] = lst[z-1].split(', ')
    i = 1
    for data in lst[z-1]:
        print(str(i) + ' ' + str(data).replace("'",
              '').replace("{", '').replace("}", ''))
        i += 1
    old = int(input('Что необходимо изменить? '))
    lst[z-1][old-1] = lst[z-1][old-1].split(': ')
    new = input('На что заменить: ')
    lst[z-1][old-1][1] = "'" + new.title() + "'"
    lst[z-1][old-1] = ': '.join(lst[z-1][old-1])
    lst[z-1] = ', '.join(lst[z-1])
    with open('employees.csv', 'w', encoding="utf-8") as data:
        data.writelines(lst)
    print('Замена выполнена.')
    print1.print_all_to_console()
