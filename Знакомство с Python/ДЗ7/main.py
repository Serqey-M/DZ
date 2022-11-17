import File_writing
import File_search

action = input('Сохранить контакт (1) или найти (2)?')
if action == '1':
    File_writing.writing_1()
    File_writing.writing_2()
elif action == '2':
    book = input('Искать в книге 1 или 2?')
    if book == '1':
        File_search.search_1()
    elif book == '2':
        File_search.search_2()
    else:
        print('Некоректный выбор')
else:
    print('Некоректный выбор')