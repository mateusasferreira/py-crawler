from base.crawler import AbstractCrawler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.chrome.options import Options

class ChromeCrawler(AbstractCrawler):

  def __init__(self):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)

  def go_to(self, url: str):
    self.driver.get(url)

  def find_element_by_id(self, id: str) -> WebElement:
    return self.driver.find_element(By.ID, id)

  def find_element_by_xpath(self, xpath: str) -> WebElement:
    return self.driver.find_element(By.XPATH, xpath)

  def click(self, element: WebElement):
    element.click()

  def input_fill(self, input: WebElement, value: str):
    input.send_keys(value)

  def get_page_content(self) -> str:
    return self.driver.page_source

