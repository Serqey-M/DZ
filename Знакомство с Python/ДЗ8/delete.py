import print1
import file_list


def delete_str():
    print1.print_all_to_console()
    lst = file_list.lst()
    z = int(input('Какую строку необходимо удалить? '))
    lst.pop(z-1)
    with open('employees.csv', 'w', encoding="utf-8") as data:
        data.writelines(lst)
    print('Удаление выполнено.')
    print1.print_all_to_console()
