from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject

class UploadApplicationPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.assertEqual(" Application :: :: Upload Application", self.driver.title)

  def select_file(self,file_path):
    driver = selenium_driver.driver
    upload_control = driver.find_element_by_id("app-file")
    upload_control.send_keys(file_path)

  def click_upload(self):
    driver = selenium_driver.driver
    driver.find_element_by_name("action").click()