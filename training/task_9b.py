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


def test_task_9a(driver):

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    rows = driver.find_elements_by_css_selector(".row")

    for index, row in enumerate(rows):
        country_index = index+2
        driver.find_element_by_xpath("//tr[" + str(country_index) + "]/td[3]/a").click()
        countries_zones = driver.find_elements_by_xpath("//table[@id='table-zones']//tr//select[contains(@name,'][zone_code]')]")
        zones_names = []

        for zone in countries_zones:
            zone = zone.find_element_by_xpath(".//option[@selected='selected']")
            zones_names.append(zone.get_attribute("textContent"))

        print(zones_names == sorted(zones_names))
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
