from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ChromeCrawler:

  def __init__(self):
    self.driver = webdriver.Chrome()

  def go_to(self, url):
    self.driver.get(url)
    time.sleep(3)

  def find_element_by_id(self, id):
    return self.driver.find_element(By.ID, id)

  def find_element_by_XPath(self, xpath):
    return self.driver.find_element(By.XPATH, xpath)

  def input_fill(self, input, value):
    input.send_keys(value)

crawler = ChromeCrawler()
