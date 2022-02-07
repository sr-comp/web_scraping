from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path='/home/srcomp/PycharmProjects/tosinso/geckodriver')
driver.get('https://www.google.com/')
driver.maximize_window()
waits = WebDriverWait(driver,20)
x_1 = waits.until(EC.visibility_of_element_located((By.TAG_NAME, 'input')))
x_1.send_keys('تست روانشناسی'+Keys.ENTER)
x_2 = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR , 'a[href="https://esanj.ir/tag/psychology-test"]'))).click()
x_3 = waits.until(EC.element_to_be_clickable((By.LINK_TEXT, 'تست احساس تنهایی (SLFS) - رایگان'))).click()
x_4 = waits.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section[2]/div/div[3]/div[2]/a[1]'))).click()
x_5 = waits.until(EC.element_to_be_clickable((By.XPATH, '//select[@name="sex"]')))
drop_1 = Select(x_5)
drop_1.select_by_value('male')
x_6 = waits.until(EC.element_to_be_clickable((By.ID, 'year_birth')))
drop_2 = Select(x_6)
drop_2.select_by_value('1368')
x_7 = waits.until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]'))).click()

for i in range(1,25):
    print('---------------')
    print("one:",i)
    if i%5 == 0:
        x_8 = waits.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="answer-5"]'))).click()
    elif i%5 == 1:
        x_9 = waits.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="answer-4"]'))).click()
    elif i%5 == 2:
        x_10 = waits.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="answer-3"]'))).click()
    elif i%5 == 3:
        x_11 = waits.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="answer-2"]'))).click()
    else:
        x_12 = waits.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="answer-1"]'))).click()

    if i == 12:
        break
    print("two:",i)
    print('###############')


# btn_2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="https://www.python.org/"]')))
# # btn_2 = driver.find_element_by_xpath('//a[@href="https://www.python.org/"]')
# btn_2.click()

