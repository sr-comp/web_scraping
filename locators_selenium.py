from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='/home/srcomp/PycharmProjects/tosinso/geckodriver')
driver.get('https://www.google.com/')
driver.maximize_window()
btn_1 = driver.find_element_by_tag_name('input')
# btn_1 = driver.find_element_by_id('input').send_keys('python')
btn_1.send_keys('python'+Keys.ENTER)
time.sleep(3)
# btn_2 = driver.find_element_by_xpath('//a[@href="https://www.python.org/"]')
# btn_2.click()
btn_2 = driver.find_element_by_css_selector('a[href="https://www.python.org/"]')
btn_2.click()

