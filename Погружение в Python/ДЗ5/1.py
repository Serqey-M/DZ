# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def file(path_file: str) -> tuple[str]:
    result0 = path_file.split('\\')[-1].split('.')
    result = (path_file, result0[0], result0[1])
    return result


if __name__ == '__main__':
    print(file('D:\GB\ДЗ\Введение в програмирование\ДЗ2\Задача 1\Код.docx'))