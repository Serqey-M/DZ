from checkers import checkout, getout
import pytest

folder_in = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"
folder_ext2 = "/home/user/folder2"


def test_step1():
    # Создание архива
    res1 = checkout("cd /{}; 7z a {}/arx2".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls /home/user/out", "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
     # Извлечение файлов из архива в текущий каталог
    res1 = checkout("cd {}; 7z e arx2.7z -y".format(folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "test1")
    res3 = checkout("ls {}".format(folder_out), "test2")
    assert res1 and res2 and res3, "test2 FAIL"


def test_step3():
    # Проверка целостностиархива
    assert checkout("cd {}; 7z t arx2.7z".format(folder_out), "Everything is Ok"), "test3 FAIL"


def test_step4():
    # Обновление файлов для архивирования
    assert checkout("cd {}; 7z u {}/arx2.7z".format(folder_in, folder_out), "Everything is Ok"), "test4 FAIL"


def test_step5():
    # Вывод списка содержимого архива
    res1 = checkout("cd {}; 7z l arx2.7z".format(folder_out), "test1")
    res2 = checkout("cd {}; 7z l arx2.7z".format(folder_out), "test2")
    assert res1 and res2, "test5 FAIL"


def test_step6():
    # Извлечение файлов из архива в указанный каталог
    res1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(folder_out, folder_ext2), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext2), "test1")
    res3 = checkout("ls {}".format(folder_ext2), "test2")
    assert res1 and res2 and res3, "test6 FAIL"


def test_step7():
    # Удаление файлов из архива
    assert checkout("cd {}; 7z d arx2.7z".format(folder_out), "Everything is Ok"), "test7 FAIL"


def test_step8():
    # Вычисление хеша файла
    res1 = checkout("cd {}; 7z h".format(folder_in), "Everything is Ok")
    hash_ = getout("cd {}; crc32".format(folder_in)).upper()
    res2 = checkout("cd {}; 7z h".format(folder_in), hash_)
    assert res1 and res2, "test8 FAIL"