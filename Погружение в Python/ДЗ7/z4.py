# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_renaming_files(directory: str, *, final_name: str = '', number_digits: int = 3, source_file_extension: str, end_file_extension: str, range_of_original_name: list[int, int]=[0,2]) -> None:
    count = 10 ** (number_digits)
    for obj in os.listdir(directory): 
        try:
            original_name = obj.split('.')
            if original_name[1] == source_file_extension:
                count += 1
                new_name = f'{original_name[0][range_of_original_name[0]:range_of_original_name[1]+1]}{final_name}{str(count)[1:]}.{end_file_extension}'
                os.rename(f'D:\GB\ДЗ\Погружение в Python\ДЗ7\directory\{obj}', f'D:\GB\ДЗ\Погружение в Python\ДЗ7\directory\{new_name}')
        except IndexError:
            continue    


if __name__ == '__main__':
    group_renaming_files('D:\GB\ДЗ\Погружение в Python\ДЗ7\directory', final_name = 'PDF', source_file_extension = 'gif', end_file_extension = 'pdf')