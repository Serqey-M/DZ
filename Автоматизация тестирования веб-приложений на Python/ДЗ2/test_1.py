from datetime import datetime
import time
import pytest
import yaml
from module import Site


with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])


def test_step1(x_selector_1, x_selector_2, btn_selector, x_selector_3, expected_result_1):
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    error_label = site.find_element('xpath', x_selector_3)
    result = error_label.text
    assert result == expected_result_1, 'test1 failed'


def test_step2(x_selector_1, x_selector_2, btn_selector, x_selector_4, expected_result_2):
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(testdata['username'])
    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', btn_selector)
    btn.click()
    link1 = site.find_element('xpath', x_selector_4)
    result = link1.text
    assert result == expected_result_2


def test_step3(btn_selector2, btn_selector3, x_selector_5, x_selector_6, x_selector_7, x_selector_8, expected_result_3):
    btn = site.find_element('css', btn_selector2)
    time.sleep(testdata['sleep_time'])
    btn.click()
    input1 = site.find_element('xpath', x_selector_5)
    input1.clear()
    title = datetime.now()
    input1.send_keys(str(title))
    input1 = site.find_element('xpath', x_selector_6)
    input1.clear()
    input1.send_keys(testdata['new_post_description'])
    input1 = site.find_element('xpath', x_selector_7)
    input1.clear()
    input1.send_keys(testdata['new_post_content'])
    btn = site.find_element('css', btn_selector3)
    btn.click() 
    time.sleep(testdata['sleep_time'])
    link = site.find_element('xpath', x_selector_8)
    result = link.text
    site.close()
    assert expected_result_3 in result


if __name__ == '__main__':
    pytest.main(['-v'])
    site.close()