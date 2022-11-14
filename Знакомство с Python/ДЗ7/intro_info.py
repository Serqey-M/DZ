def info1():
    info = dict()
    surname = input('Введите фамилию: ')
    info['Фамилия'] = surname
    name = input('Введите имя: ')
    info['Имя'] = name
    patronymic = input('Введите Отчество: ')
    info['Отчество'] = patronymic
    phone_number = '+7'
    x = False
    while not x:
        try:
            number = input('Введите номер телефона: ')
            if len(number) != 10:
                print('В номере телефона должен содержать 10 цифр')
            else:
                number = int(number)
                x = True
        except:
            print('Не коректный номер телефона')
    phone_number+=str(number)
    info['Номер телефона'] = phone_number
    description = input('Введите описание: ')
    info['Описание'] = description
    return info