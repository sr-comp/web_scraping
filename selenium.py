from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/home/srcomp/PycharmProjects/tosinso/geckodriver')
driver.get('https://www.varzesh3.com/')
driver.maximize_window()
time.sleep(10)
driver.get('https://www.digikala.com/')
driver.back()
time.sleep(10)
driver.forward()
driver.close()