import yaml
from sshcheckers import upload_files, ssh_checkout, ssh_checkout_negative

with open('config.yaml') as f:
    data = yaml.safe_load(f)

folder_out = f"{data['folder']}/badarx"
folder_in = f"{data['folder']}/file"


def test_step0():
    res = []
    upload_files(data['host'], data['user'], "11", '{}/p7zip-full.deb'.format(data['local_path']),
                 '{}/p7zip-full.deb'.format(data['remoute_path']))
    res.append(ssh_checkout(data['host'], data['user'], "11", "echo '11' | sudo -S dpkg -i {}/p7zip-full.deb"
                            .format(data['local_path']), "Настраивается пакет"))
    res.append(ssh_checkout(data['host'], data['user'], "11", "echo '11' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    assert all(res)


def test_step1(make_badarx):
    # test1
    assert ssh_checkout_negative(data['host'], data['user'], "11", "cd {}; 7z e badarx.7z -y".format(folder_out), "ERROR"), "Test1 Fail"


def test_step2(make_badarx):
    # test2
    assert ssh_checkout_negative(data['host'], data['user'], "11", "cd {}; 7z t badarx.7z".format(folder_out), "ERROR"), "Test2 Fail"


def test_step3(make_folders, make_files):
    # Создание архива
    assert ssh_checkout_negative(data['host'], data['user'], "11", "cd {}; 7z a -tzp {}/arx1".format(folder_in, folder_out), "ERROR"), "Test3 Fail"


