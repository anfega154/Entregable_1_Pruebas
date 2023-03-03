from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time


options= webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path='C:\\Users\\Andrés\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver=webdriver.Chrome(driver_path,chrome_options=options)

driver.get('https://buggy.justtestit.org/')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'a.btn btn-success-outline'.replace(' ', '.'))))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#username')))\
    .send_keys('Anfega')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#firstName')))\
    .send_keys('Andres')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#lastName')))\
    .send_keys('Gañan')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#password')))\
    .send_keys('Af123456*')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#confirmPassword')))\
    .send_keys('Af123456*')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.btn btn-default'.replace(' ', '.'))))\
    .click()

texto=WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.result alert alert-danger'.replace(' ', '.'))))
texto = texto.text

print("\n"+texto)
time.sleep(20)