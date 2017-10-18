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

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    rows = driver.find_elements_by_css_selector(".row")
    countries_names = []
    countries_with_zones = []

    for index, row in enumerate(rows):
        country_element = row.find_element_by_tag_name("a")
        countries_names.append(country_element.get_attribute("textContent"))

        zone = row.find_elements_by_tag_name("td")[5].get_attribute("textContent")
        if int(zone) > 0:
            countries_with_zones.append(index)

    print(countries_names == sorted(countries_names))

    for country_index in countries_with_zones:
        countries_zones = []

        driver.find_element_by_xpath("//tr[" + str(country_index+2) + "]/td[7]").click()
        zones = driver.find_elements_by_xpath("//table[@id='table-zones']//td[3]//input[@type='hidden']")

        for zone in zones:
            countries_zones.append(zone.get_attribute("textContent"))

        print(countries_zones == sorted(countries_zones))

        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
