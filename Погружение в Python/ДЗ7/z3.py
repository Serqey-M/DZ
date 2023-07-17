# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os


def sort (directory: str, *args: dict[str: list[str]]) -> None:
    for i in args:
        if os.path.isdir(f'{directory}\{str(i.keys())[12:-3]}') == False:
            os.mkdir(f'{directory}\{str(i.keys())[12:-3]}')
        for obj in os.listdir(directory):
            try:
                if (obj.split('.'))[1] in list(i.values())[0]:
                    os.replace(f'{directory}\{obj}', f'{directory}\{str(i.keys())[12:-3]}\{obj}')
            except IndexError:
                continue

    
if __name__ == '__main__':
    sort('D:\GB\ДЗ\Погружение в Python\ДЗ7\directory', {'видео': ['mp4', 'avi']}, {'изображения': ['jpg', 'png']}, {'текст': ['txt', 'doc']})