import intro_info

info= intro_info.info()
# print(info)

def writing_1 ():
    with open ('Phonebook_1.txt', 'a', encoding='utf-16') as file:
        file.write(str(info))

def writing_2 ():
    with open ('Phonebook_2.txt', 'a', encoding='utf-16') as file:
        file.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nОтчество: {info[2]}\n\nНомер телефона:{(info[3])}\n\n Описание:{info[4]}\n\n')

# writing_1 ()

# writing_2 ()