# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_task_10a(driver):

    driver.get("http://localhost/litecart/en/")
    product = driver.find_element_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']/a")
    product_title1 = product.find_element_by_xpath(".//div[@class='name']").text
    product.click()
    product_title2 = driver.find_element_by_xpath(".//div[@id='box-product']//h1[@class='title']").text
    print(product_title1 == product_title2)

def test_task_10b(driver):

    driver.get("http://localhost/litecart/en/")
    product = driver.find_element_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']/a")
    product_reg_price1 = product.find_element_by_xpath(".//s[@class='regular-price'] ").text
    product_sale_price1 = product.find_element_by_xpath(".//strong[@class='campaign-price']").text
    product.click()
    product_reg_price2 = driver.find_element_by_xpath("//s[@class='regular-price']").text
    product_sale_price2 = driver.find_element_by_xpath("//strong[@class='campaign-price']").text
    print(product_reg_price1 == product_reg_price2)
    print(product_sale_price1 == product_sale_price2)

def test_task_10c(driver):

    line = 'line-through'
    driver.get("http://localhost/litecart/en/")
    product = driver.find_element_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']/a")
    reg_price_color1 = product.find_element_by_xpath(".//s[@class='regular-price'] ").value_of_css_property("color")

    if len(reg_price_color1) == 22:
        red_reg_price_color = reg_price_color1[5:8]
        green_reg_price_color = reg_price_color1[10:13]
        blue_reg_price_color = reg_price_color1[15:18]
        print(red_reg_price_color == green_reg_price_color == blue_reg_price_color)

    if len(reg_price_color1) == 18:
        red_reg_price_color = reg_price_color1[4:7]
        green_reg_price_color = reg_price_color1[9:12]
        blue_reg_price_color = reg_price_color1[14:17]
        print(red_reg_price_color == green_reg_price_color == blue_reg_price_color)

    reg_price_line = product.find_element_by_xpath(".//s[@class='regular-price']").value_of_css_property("text-decoration-line")
    print(reg_price_line == line)

    if reg_price_line == (""):
        reg_price_line = product.find_element_by_xpath(".//s[@class='regular-price']").value_of_css_property("text-decoration")
        print(reg_price_line == line)

    product.click()
    reg_price_color2 = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("color")

    if len(reg_price_color2) == 22:
        red_reg_price_color = reg_price_color2[5:8]
        green_reg_price_color = reg_price_color2[10:13]
        blue_reg_price_color = reg_price_color2[15:18]
        print(red_reg_price_color == green_reg_price_color == blue_reg_price_color)

    if len(reg_price_color2) == 18:
        red_reg_price_color = reg_price_color2[4:7]
        green_reg_price_color = reg_price_color2[9:12]
        blue_reg_price_color = reg_price_color2[14:17]
        print(red_reg_price_color == green_reg_price_color == blue_reg_price_color)

def test_task_10d(driver):

    font_weight = 'bold'
    font_weight_ff = '900'
    driver.get("http://localhost/litecart/en/")
    product = driver.find_element_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']/a")
    sale_price_weight = product.find_element_by_xpath(".//strong[@class='campaign-price']").value_of_css_property("font-weight")
    print (sale_price_weight == font_weight or sale_price_weight == font_weight_ff)

def test_task_10e(driver):

    driver.get("http://localhost/litecart/en/")
    product = driver.find_element_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']/a")
    sale_price_color1 = product.find_element_by_xpath(".//strong[@class='campaign-price']").value_of_css_property("color")

    if len(sale_price_color1) == 14:
        red_sale_price_color = sale_price_color1[4:7]
        green_sale_price_color = sale_price_color1[9:10]
        blue_sale_price_color = sale_price_color1[12:13]
        print(red_sale_price_color != green_sale_price_color == blue_sale_price_color == '0')

    if len(sale_price_color1) == 18:
        red_sale_price_color = sale_price_color1[5:8]
        green_sale_price_color = sale_price_color1[10:11]
        blue_sale_price_color = sale_price_color1[13:14]
        print(red_sale_price_color != green_sale_price_color == blue_sale_price_color == '0')

    product.click()
    sale_price_color2 = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("color")

    if len(sale_price_color2) == 14:
        red_sale_price_color = sale_price_color2[4:7]
        green_sale_price_color = sale_price_color2[9:10]
        blue_sale_price_color = sale_price_color2[12:13]
        print(red_sale_price_color != green_sale_price_color == blue_sale_price_color == '0')

    if len(sale_price_color2) == 18:
        red_sale_price_color = sale_price_color2[5:8]
        green_sale_price_color = sale_price_color2[10:11]
        blue_sale_price_color = sale_price_color2[13:14]
        print(red_sale_price_color != green_sale_price_color == blue_sale_price_color == '0')


def test_task_10f(driver):
    
    driver.get("http://localhost/litecart/en/")
    product = driver.find_element_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']/a")
    sale_price_size1 = product.find_element_by_xpath(".//strong[@class='campaign-price']").value_of_css_property("font-size")
    reg_price_size1 = product.find_element_by_xpath(".//s[@class='regular-price'] ").value_of_css_property("font-size")
    print (reg_price_size1 < sale_price_size1)
    product.click()
    reg_price_size2 = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property("font-size")
    sale_price_size2 = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property("font-size")
    print (reg_price_size2 < sale_price_size2)