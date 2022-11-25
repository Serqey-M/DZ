import os


def Search_Entry():
    with open('employees.csv', 'r', encoding='utf-8') as data:
        name = input('Искать: ').lower()
        os.system('CLS')
        for line in data:
            if name in line.lower():
                print(line.replace("'", ''))
