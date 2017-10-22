# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import sys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_task_11(driver):

    random_index = str(int(time.time()))
    random_email = "iryna.buldakova+" + random_index + "@gmail.com"

    driver.get("http://localhost/litecart/en/create_account")
    driver.find_element_by_name("tax_id").send_keys(random_index)
    driver.find_element_by_name("firstname").send_keys(random_index)
    driver.find_element_by_name("lastname").send_keys(random_index)
    driver.find_element_by_name("address1").send_keys(random_index)
    driver.find_element_by_name("postcode").send_keys(random_index[0:5])
    driver.find_element_by_name("city").send_keys(random_index)
    Select(driver.find_element_by_xpath("//form[@name='customer_form']//td/select[@name='country_code']")).select_by_value('US')
    Select(driver.find_element_by_xpath("//form[@name='customer_form']//select[@name='zone_code']")).select_by_value('AL')
    driver.find_element_by_name("email").send_keys(random_email)
    driver.find_element_by_name("phone").send_keys("+123" + random_index)
    driver.find_element_by_name("password").send_keys(random_index)
    driver.find_element_by_name("confirmed_password").send_keys(random_index)
    driver.find_element_by_name("create_account").click()
    driver.get("http://localhost/litecart/en/logout")

    driver.find_element_by_name("email").send_keys(random_email)
    driver.find_element_by_name("password").send_keys(random_index)
    driver.find_element_by_name("login").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-account")))

