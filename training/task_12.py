# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import sys
import os
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_12(driver):

    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    random_index = str(int(time.time()))
    date_from = date.today().strftime("%m-%d-%Y")
    date_to = (date.today()+timedelta(days=30)).strftime("%m-%d-%Y")

    driver.get("http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product")
    driver.find_element_by_xpath("//div[@id='tab-general']//label/input[@value='1']").click()
    driver.find_element_by_name("name[en]").send_keys(random_index)
    driver.find_element_by_name("code").send_keys(random_index)
    driver.find_element_by_xpath("//div[@class='input-wrapper']//tr[2]//input[@name='categories[]']").click()
    Select(driver.find_element_by_xpath("//div[@id='tab-general']//select[@name='default_category_id']")).select_by_value('1')
    driver.find_element_by_xpath("//div[@class='input-wrapper']//input[@value='1-1']").click()
    driver.find_element_by_name("quantity").send_keys(Keys.HOME + "5")
    driver.find_element_by_name("new_images[]").send_keys(os.getcwd() + '/images/product.png')
    driver.find_element_by_name("date_valid_from").send_keys(date_from)
    driver.find_element_by_name("date_valid_to").send_keys(date_to)

    driver.find_element_by_xpath("//div[@class='tabs']/ul/li[2]").click()
    driver.find_element_by_name("keywords").send_keys(random_index)
    driver.find_element_by_name("short_description[en]").send_keys(random_index)
    driver.find_element_by_class_name("trumbowyg-editor").send_keys(random_index)
    driver.find_element_by_name("head_title[en]").send_keys(random_index)
    driver.find_element_by_name("meta_description[en]").send_keys(random_index)

    driver.find_element_by_xpath("//div[@class='tabs']/ul/li[4]").click()
    driver.find_element_by_name("purchase_price").send_keys(Keys.HOME + "60")
    Select(driver.find_element_by_name("purchase_price_currency_code")).select_by_value('USD')
    driver.find_element_by_name("prices[USD]").send_keys(Keys.HOME + "70")
    driver.find_element_by_name("prices[EUR]").send_keys(Keys.HOME + "90")
    driver.find_element_by_name("save").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[3]//*[text()=" + str(random_index) + "]")))

