import pytest
import yaml
from datetime import datetime

with open('testdata.yaml', encoding='utf-8') as f:
    userdata = yaml.safe_load(f)
    username = userdata['username']


@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def expected_result_1():
    return '401'


@pytest.fixture()
def x_selector_4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def expected_result_2():
    return f'Hello, {username}' 


@pytest.fixture()
def btn_selector2():
    return """.button-block.svelte-1e9zcmy"""


@pytest.fixture()
def x_selector_5():
    return """/html/body/div/main/div/div/form/div/div/div[1]/div/label/input"""


@pytest.fixture()
def x_selector_6():
    return """/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def x_selector_7():
    return """/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def btn_selector3():
    return """.button"""


@pytest.fixture()
def x_selector_8():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def expected_result_3():
    return str(datetime.now().strftime("%Y-%m-%d"))



