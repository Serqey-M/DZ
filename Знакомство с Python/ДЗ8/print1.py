def print_all_to_console():
    i = 1
    print('_________________________________________________\n')
    with open('employees.csv', encoding="utf-8") as data:
        for line in data:
            print(str(i) + ' ' + line.replace("'", ''))
            i += 1
    print('_________________________________________________')
