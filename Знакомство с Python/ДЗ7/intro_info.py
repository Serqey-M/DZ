def info ():
    info = []
    surname = input('Введите фамилию: ')
    info.append(surname)
    name = input('Введите имя: ')
    info.append(name)
    patronymic = input('Введите Отчество: ')
    info.append(patronymic)
    phone_number = '+7'
    x = False
    while not x:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 10:
                print('В номере телефона должен содержать 10 цифр')
            else:
                phone_number = int(phone_number)
                x = True
        except:
            print('Не коректный номер телефона')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

# x= info()   
# print(x) 
# print(x[3])
# # z = open('text.txt', 'a')
# # z.write(str(x))
# # z.close()