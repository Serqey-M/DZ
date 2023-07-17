# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from random import choices, randint
from string import ascii_lowercase, digits


def gen_ext(directory: str, *args: str, name_len_min: int=6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096, num_files: int = 41) -> None:
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    for _ in range (num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k = randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        try:
             with open(f'{directory}\{name}.{(choices(args))[0]}', 'xb') as f:
                f.write(data)
        except FileExistsError:
            continue


if __name__ == '__main__':
    gen_ext('D:\GB\ДЗ\Погружение в Python\ДЗ7\directory','txt', 'pdf', 'jpg', 'doc', 'avi', 'mp4', 'png', 'gif')    