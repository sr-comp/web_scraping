from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox(executable_path='/home/srcomp/PycharmProjects/tosinso/geckodriver')
        self.username = username
        self.password = password

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        driver.maximize_window()
        name = driver.find_element_by_name('username').send_keys(self.username)
        pas = driver.find_element_by_name('password').send_keys(self.password)
        btn_1 = driver.find_element_by_css_selector('button[type="submit"]').click()
        time.sleep(3)
        btn_2 = driver.find_element_by_css_selector('button[type="submit"]').click()
        time.sleep(3)
        btn_3 = driver.find_element_by_css_selector('button.Holwn').click()

username = "test"
password = "testtest"
test = Bot(username, password)
test.Login()

