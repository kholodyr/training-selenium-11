# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Safari()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.ru/")
    driver.find_element_by_name("q").send_keys("webdriver", Keys.ENTER)
    #driver.find_element_by_name("btnK").click()
    WebDriverWait(driver, 10).until(EC.title_contains("webdriver - Поиск в Google"))
