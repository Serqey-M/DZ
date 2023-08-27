import logging
import random
import string
from datetime import datetime
import pytest
import yaml
from sshcheckers import ssh_checkout, ssh_getout

with open('config.yaml') as f:
    data = yaml.safe_load(f)

logging.basicConfig(level=20, filename=f'{data["folder_log"]}/stat.txt', encoding='utf-8', style='{')
logger = logging.getLogger(__name__)

folder_in = f"{data['folder']}/file"
folder_out = f"{data['folder']}/out"
folder_ext = f"{data['folder']}/ext"
folder_badarx = f"{data['folder']}/badarx"


@pytest.fixture()
def make_folders():
    # Создание директорий
    ssh_checkout(data['host'], data['user'], "11", "mkdir {} {} {} {}".format(data['folder'], folder_in, folder_out, folder_ext), "")
    ssh_checkout(data['host'], data['user'], "11", "rm -rf {}/* {}/* {}/*".format(folder_in, folder_out, folder_ext), "")
    yield
    ssh_checkout(data['host'], data['user'], "11", "rm -rf {}".format(data['folder']), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data['count_file']):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data['size_name_file']))
        if ssh_checkout(data['host'], data['user'], "11", "cd {}; dd if=/dev/urandom of={} bs={}M count=1 iflag=fullblock".format(folder_in, filename, data['size_file']), ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not ssh_checkout(data['host'], data['user'], "11", "cd {}; mkdir {}".format(folder_in, subfoldername), ""):
        return None, None
    if not ssh_checkout(data['host'], data['user'], "11", "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(folder_in, subfoldername, testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_badarx():
    ssh_checkout(data['host'], data['user'], "11", "mkdir {} {}".format(data['folder'], folder_badarx), "")
    ssh_checkout(data['host'], data['user'], "11", "cd {}; 7z a {}/badarx.7z".format(folder_in, folder_badarx), "Everything is Ok")
    ssh_checkout(data['host'], data['user'], "11", "truncate -s 1 {}/badarx.7z".format(folder_badarx), "Everything is Ok")
    yield
    ssh_checkout(data['host'], data['user'], "11", "rm -rf {}".format(data['folder']), "")


@pytest.fixture(autouse=True)
def log():
    stat = ssh_getout(data['host'], data['user'], "11", "cat /proc/loadavg")
    yield
    logger.info(f'{datetime.now()}: кол-во файлов из config - {data["count_file"]}; '
                f'размер файла из config - {data["size_file"]}, статистика загрузки процессора - {stat}')


@pytest.fixture(autouse=True)
def save_log():
    with open('{}/stat2.txt'.format(data["folder_log2"]), 'w') as f:
        f.write(ssh_getout(data['host'], data['user'], "11", 'sudo journalctl -S11 --since "{}" --until "{}"'.format(data['date1'], data['date2'])))


@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")