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


def test_task_17(driver):

    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    products = driver.find_elements_by_css_selector("table.dataTable tr td:nth-child(3) a[href*='product']")
    for i in range(len(products)):
        products = driver.find_elements_by_css_selector("table.dataTable tr td:nth-child(3) a[href*='product']")
        products[i].click()
        for l in driver.get_log("browser"):
            print(l)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
