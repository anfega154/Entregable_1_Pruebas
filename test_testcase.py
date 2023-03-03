# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestcase():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcase(self):
    self.driver.get("https://buggy.justtestit.org/")
    self.driver.set_window_size(1296, 688)
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    element = self.driver.find_element(By.LINK_TEXT, "Register")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("anfega141")
    self.driver.find_element(By.ID, "username").send_keys("anfega142")
    self.driver.find_element(By.ID, "firstName").click()
    self.driver.find_element(By.ID, "firstName").send_keys("Andres Felipe ")
    self.driver.find_element(By.ID, "lastName").click()
    self.driver.find_element(By.ID, "lastName").send_keys("Gañan Moreno ")
    self.driver.find_element(By.ID, "password").click()
    element = self.driver.find_element(By.ID, "password")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "password").click()
    element = self.driver.find_element(By.ID, "password")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "password").send_keys("Aa5592770")
    self.driver.find_element(By.ID, "confirmPassword").click()
    element = self.driver.find_element(By.ID, "confirmPassword")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "confirmPassword").send_keys("Aa5592770")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Aa5592770*")
    self.driver.find_element(By.ID, "confirmPassword").click()
    self.driver.find_element(By.ID, "confirmPassword").send_keys("Aa5592770*")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
  