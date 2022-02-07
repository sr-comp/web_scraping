from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random
import requests

driver = webdriver.Firefox(executable_path='/home/srcomp/PycharmProjects/tosinso/geckodriver')
driver.get('https://quotes.toscrape.com/scroll')
driver.maximize_window()
time.sleep(3)
# window.scrollTo---> Java Script
# driver.execute_script('window.scrollTo(0,400)')
end_of_scroll = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(5)
    my_scroll = driver.execute_script('return document.body.scrollHeight')
    print('-----> ', my_scroll)
    if my_scroll == end_of_scroll:
        print('end')
        break
    end_of_scroll = my_scroll
text = driver.find_elements_by_css_selector('span.text')
for t in text:
    print(t.text)