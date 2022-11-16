import os

def search_1():
    with open('Phonebook_1.txt', 'r', encoding='utf-16') as file:
        sought = input('искать: ').lower()
        os.system('CLS')
        for data in file:
            if sought in data.lower():
                print(data)

def search_2():
    with open('Phonebook_2.txt', 'r', encoding='utf-16') as file:
        sought = input('искать: ').lower()
        os.system('CLS')
        temp = ''
        for data in file:
            if data!='\n':
                temp+=data.lower()
            elif sought in temp:
                print(temp)
                temp=''
            else:
                temp=''