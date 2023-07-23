# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import csv
import json
import os
import pickle


def size(directory: str) -> float:
    size = 0
    if os.path.isfile(directory):
        size += os.path.getsize(directory)
    for i in os.walk(directory):
        for j in i[2]:
            size += os.path.getsize(str(f'{i[0]}\{j}'))
    return size


def information(directory):
    path = os.path.split(directory)
    if os.path.isdir(directory):
        type_ = 'директория'
    else:
        type_ = 'файл'
    dct = {'родительская директория': path[0], 'тип': type_, 'размер': size(directory)}
    return dct


def dir_walker_(directory, dct = None):
    if dct is None:
        dct = {}
    for item in os.listdir(directory):
        check_path = os.path.join(directory, item)
        dct[item] = {'информация': information(check_path)}
        if os.path.isdir(check_path):
            dir_walker_(check_path, dct[item])
    return dct


def dir_walker(directory: str, dct = None ) -> dict[str, dict[str]]:
    path = os.path.split(directory)
    if dct is None:
        dct = {directory: {'имя': path[1], 'родительская директория': path[0], 'тип': 'директория', 'размер': size(directory)}}
    for item in os.listdir(directory):
        check_path = os.path.join(directory, item)
        if os.path.isfile(check_path):
            dct[check_path] ={'имя': item, 'родительская директория': directory, 'тип': 'файл', 'размер': size(check_path)}
        elif os.path.isdir(check_path):
            dct[check_path] = {'имя': item, 'родительская директория': directory, 'тип': 'директория', 'размер': size(check_path)}
            dir_walker(check_path, dct)
    return dct


def jsn_writer(directory: str) -> None:
    with open('D:\GB\ДЗ\Погружение в Python\ДЗ8\\file.json', 'w', encoding='utf-8') as f:
        json.dump(dir_walker_(directory), f, ensure_ascii=False, indent=2)


def csv_writer(directory: str) -> None:
    dct = dir_walker(directory)
    all_data = []
    for _, j in dct.items():
        all_data.append(j)
    with open('D:\GB\ДЗ\Погружение в Python\ДЗ8\\file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['имя', 'родительская директория', 'тип', 'размер'],dialect='excel-tab', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(all_data)


def pcl_writer(directory: str) -> None:
    dct = dir_walker(directory)
    with open('D:\GB\ДЗ\Погружение в Python\ДЗ8\\file.pickle', 'wb') as f:
        pickle.dump(dct, f)


if __name__ == '__main__':
    jsn_writer('D:\\GB\\ДЗ\\Погружение в Python')
    csv_writer('D:\\GB\\ДЗ\\Погружение в Python')
    pcl_writer('D:\\GB\\ДЗ\\Погружение в Python')
