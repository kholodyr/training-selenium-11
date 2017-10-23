# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)#seconds
    request.addfinalizer(wd.quit)
    return wd


def test_task_13(driver):

    driver.get("http://localhost/litecart/en/")

    for index in range(1,4):

        product = driver.find_element_by_xpath("//div[@id='box-most-popular']//ul/li[" + str(index) + "]/a[1]")
        product.click()

        if driver.find_elements_by_xpath("//div[@class='buy_now']//td[@class='options']"):
            Select(driver.find_element_by_name("options[Size]")).select_by_value('Small')

        driver.find_element_by_name("add_cart_product").click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(index)))
        driver.get("http://localhost/litecart/en/")

    driver.get("http://localhost/litecart/en/checkout")

    cart = driver.find_elements_by_xpath("//table[@class='dataTable rounded-corners']//td[@class='item']")

    for item in cart:
        print item
        driver.find_element_by_name("remove_cart_item").click()
        WebDriverWait(driver, 10).until(EC.staleness_of(item))
