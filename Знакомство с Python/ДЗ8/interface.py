import delete
import write
import print1
import edit
import search
import file_sorting

while True:
    try:
        print("\nМеню\n")
        print('1. Вывести все записи.\n2. Добавить запись.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Сортировать.\n7. Выход')

        value = int(input())
        if value == 1:
            print1.print_all_to_console()
        elif value == 2:
            write.New_Entry()
        elif value == 3:
            search.Search_Entry()
        elif value == 4:
            edit.Edit_Entry()
        elif value == 5:
            delete.delete_str()
        elif value == 6:
            file_sorting.sorting()
        elif value == 7:
            break
    except:
        print('')