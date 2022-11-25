def New_Entry():
    info = dict()
    surname = input('Введите фамилию: ')
    info['Фамилия'] = surname.title()
    name = input('Введите имя: ')
    info['Имя'] = name.title()
    patronymic = input('Введите Отчество: ')
    info['Отчество'] = patronymic.title()

    department = input('Введите отдел: ')
    info['Отдел'] = department.title()

    position = input('Введите должность: ')
    info['Должность'] = position.title()

    i = 1
    z = 'Y'
    while z == 'Y' or z == 'Д':
        phone_number = '+7'
        x = False
        while not x:
            try:
                number = input('Введите номер телефона: ')
                if len(number) == 11 and number[0] == '8':
                    number = number[1:]
                elif len(number) == 12 and number[:2] == '+7':
                    number = number[2:]
                if len(number) != 10:
                    print('Не коректный номер телефона')
                else:
                    number = int(number)
                    x = True
            except:
                print('Не коректный номер телефона')
        phone_number += str(number)
        info[f'Номер телефона {i}'] = phone_number
        i += 1
        z = input(
            'Желаете ввести еще один номер? (да = Y или Д; нет - любая клавиша): ').upper()

    with open('employees.csv', 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
