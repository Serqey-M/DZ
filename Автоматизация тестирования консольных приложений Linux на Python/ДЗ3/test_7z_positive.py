import yaml
from checkout import checkout_positive, getout

with open('config.yaml') as f:
    data = yaml.safe_load(f)

folder_in = f"{data['folder']}/file"
folder_out = f"{data['folder']}/out"
folder_ext = f"{data['folder']}/ext"


def test_step1(make_folders, make_files):
    # Создание архива
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok"),
           checkout_positive("ls {}".format(folder_out), "arx1.{}".format(data['type']))]
    assert all(res)


def test_step2(make_folders, make_files):
    # Извлечение файлов из архива в текущий каталог
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok"),
           checkout_positive("cd {}; 7z e arx1.{} -y".format(folder_out, data['type']), "Everything is Ok")]
    for item in make_files:
        res.append(checkout_positive("ls {}".format(folder_out), item))
    assert all(res)


def test_step3(make_folders, make_files):
    # Проверка целостностиархива
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok"),
           checkout_positive("cd {}; 7z t {}/arx1.{}".format(folder_in, folder_out, data['type']), "Everything is Ok")]
    assert all(res)


def test_step4(make_folders, make_files):
    # Обновление файлов для архивирования
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok"),
           checkout_positive("cd {}; 7z u {}/arx1.{}".format(folder_in, folder_out, data['type']), "Everything is Ok")]
    assert all(res)


def test_step5(make_folders, make_files):
    # Вывод списка содержимого архива
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok")]
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.{}".format(folder_out, data['type']), item))
    assert all(res)


def test_step6(make_folders, make_files):
    # Извлечение файлов из архива в указанный каталог
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok"),
           checkout_positive("cd {}; 7z x arx1.{} -o{} -y".format(folder_out, data['type'], folder_ext), "Everything is Ok")]
    assert all(res)


def test_step7(make_folders, make_files):
    # Удаление файлов из архива
    res = [checkout_positive("cd {}; 7z a -t{} {}/arx1".format(folder_in, data['type'], folder_out), "Everything is Ok"),
           checkout_positive("7z d {}/arx1.{}".format(folder_out, data['type']), "Everything is Ok")]
    assert all(res)


def test_step8(make_folders, make_files):
    # Вычисление хеша файла
    res = [checkout_positive("cd {}; 7z h".format(folder_in), "Everything is Ok")]
    hash_ = getout("cd {}; crc32".format(folder_in)).upper()
    res.append(checkout_positive("cd {}; 7z h".format(folder_in), hash_))
    assert all(res)


def test_step9(make_folders, make_files):
    # Создание архива
    res = [checkout_positive("cd {}; 7z a {}/arx1".format(folder_in, folder_out), "Everything is Ok"),
           checkout_positive("ls {}".format(folder_out), "arx1.7z")]
    assert all(res)
