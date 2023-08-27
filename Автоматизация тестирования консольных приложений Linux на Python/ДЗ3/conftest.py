import logging
import random
import string
from datetime import datetime
import pytest
import yaml
from checkout import checkout_positive, getout

with open('config.yaml') as f:
    data = yaml.safe_load(f)

logging.basicConfig(level=0, filename=f'{data["folder_log"]}/stat.txt', encoding='utf-8', style='{')
logger = logging.getLogger(__name__)

folder_in = f"{data['folder']}/file"
folder_out = f"{data['folder']}/out"
folder_ext = f"{data['folder']}/ext"
folder_badarx = f"{data['folder']}/badarx"


@pytest.fixture()
def make_folders():
    # Создание директорий
    checkout_positive("mkdir {} {} {} {}".format(data['folder'], folder_in, folder_out, folder_ext), "")
    checkout_positive("rm -rf {}/* {}/* {}/*".format(folder_in, folder_out, folder_ext), "")
    yield
    checkout_positive("rm -rf {}".format(data['folder']), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data['count_file']):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=data['size_name_file']))
        if checkout_positive(
                "cd {}; dd if=/dev/urandom of={} bs={}M count=1 iflag=fullblock".format(folder_in, filename,
                                                                                        data['size_file']),
                ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive("cd {}; mkdir {}".format(folder_in, subfoldername), ""):
        return None, None
    if not checkout_positive(
            "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(folder_in, subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_badarx():
    checkout_positive("mkdir {} {}".format(data['folder'], folder_badarx), "")
    checkout_positive("cd {}; 7z a {}/badarx.7z".format(folder_in, folder_badarx), "Everything is Ok")
    checkout_positive("truncate -s 1 {}/badarx.7z".format(folder_badarx), "Everything is Ok")
    yield
    checkout_positive("rm -rf {}".format(data['folder']), "")


@pytest.fixture(autouse=True)
def log():
    stat = getout("cat /proc/loadavg")
    yield
    logger.info(f'{datetime.now()}: кол-во файлов из config - {data["count_file"]}; '
                f'размер файла из config - {data["size_file"]}, статистика загрузки процессора - {stat}')
