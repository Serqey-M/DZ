import intro_info

def writing():
    info = intro_info.info()
    
    with open('Phonebook_1.txt', 'a', encoding='utf-16') as file:
        file.write(f'{info}\n\n')

    with open('Phonebook_2.txt', 'a', encoding='utf-16') as file:
        for i,j in info.items():
            file.writelines(f'{i}: {j}\n')
        file.writelines(f'\n')