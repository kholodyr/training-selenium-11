# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_7(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar")))

    amount = driver.find_elements_by_xpath("//li[@id='app-']/a")

    for i in range(0, len(amount)):
        index = i + 1
        driver.find_element_by_xpath("//li[@id='app-'] [" + str(index) + "]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td#content h1")))
        amount_sub = driver.find_elements_by_xpath("//li[@id='app-']/ul/li/a")
        if len(amount_sub) > 0:
            for ie in range(0, len(amount_sub)):
                index_sub = ie + 1
                driver.find_element_by_xpath("//li[@id='app-'] [" + str(index) + "]/ul/li[" + str(index_sub) + "]/a").click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td#content h1")))
