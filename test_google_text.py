import os
from selenium import webdriver

def test_google():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://google.com')
    elm = driver.find_element_by_name('q')
    elm.clear()
    elm.send_keys('hogehoge')
    assert elm.get_attribute('value') == 'hogehoge'
    driver.close()
