import pytest
from selenium import webdriver
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

reload(sys)
sys.setdefaultencoding('utf-8')


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task_14(driver):

    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.get("http://localhost/litecart/admin/?app=countries&doc=edit_country")
    links = driver.find_elements_by_xpath("//i[@class='fa fa-external-link']")

    for link in links:
        main_window = driver.window_handles[0]
        link.click()
        WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to_window(new_window)
        driver.close()
        driver.switch_to_window(main_window)
