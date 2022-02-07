from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='/home/srcomp/PycharmProjects/tosinso/geckodriver')
driver.get('https://www.google.com/')
driver.implicitly_wait(10)
driver.maximize_window()
btn_1 = driver.find_element_by_tag_name('input')
btn_1.send_keys('python'+Keys.ENTER)
btn_2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="https://www.python.org/"]')))
# btn_2 = driver.find_element_by_xpath('//a[@href="https://www.python.org/"]')
btn_2.click()

