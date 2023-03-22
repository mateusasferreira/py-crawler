from abc import ABC, abstractmethod

class AbstractCrawler(ABC):

  @abstractmethod
  def go_to(self, url):
    pass

  @abstractmethod
  def find_element_by_id(self, id):
    pass

  @abstractmethod
  def find_element_by_xpath(self, xpath):
    pass

  @abstractmethod
  def input_fill(self, input, value):
    pass

  @abstractmethod
  def click(self, element):
    pass

  @abstractmethod
  def input_fill(self, input: any, value):
    pass

  @abstractmethod
  def get_page_content(self):
    pass