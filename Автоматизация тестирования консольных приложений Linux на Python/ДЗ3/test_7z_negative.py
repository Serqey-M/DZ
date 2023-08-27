import yaml

from checkout import checkout_negative, checkout_positive

with open('config.yaml') as f:
    data = yaml.safe_load(f)

folder_out = f"{data['folder']}/badarx"
folder_in = f"{data['folder']}/file"


def test_step1(make_badarx, log):
    # test1
    assert checkout_negative("cd {}; 7z e badarx.7z -y".format(folder_out), "ERROR"), "Test1 Fail"


def test_step2(make_badarx):
    # test2
    assert checkout_negative("cd {}; 7z t badarx.7z".format(folder_out), "ERROR"), "Test2 Fail"


def test_step3(make_folders, make_files):
    # Создание архива
    assert checkout_negative("cd {}; 7z a -tzp {}/arx1".format(folder_in, folder_out), "ERROR"), "Test3 Fail"


