# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_7(driver):
    driver.get("http://localhost/litecart/en/")

    products = driver.find_elements_by_css_selector("li[class*='product']")

    for product in products:
        stickers = product.find_elements_by_css_selector("div[class*='sticker']")
        if len(stickers) == 1:
            print 'Pass'
            return True
        else:
            print 'Fail'
            return False
