# Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits


def gen_ext(ext: str, name_len_min: int=6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096, num_files: int = 41) -> None:
    for _ in range (num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def gen_ext_n(*args: str, num_files: int) -> None:
    for _ in range(num_files):
        gen_ext(*(choices(args)), num_files = 1)


if __name__ == '__main__':
    gen_ext_n('txt', 'pdf', 'jpg', 'doc', num_files = 5)