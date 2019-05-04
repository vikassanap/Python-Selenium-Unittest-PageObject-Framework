from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject

class MyApplicationsPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.assertEqual("Application :: Your Applications", self.driver.title)

  def click_upload_link(self):
    driver = selenium_driver.driver
    driver.find_element_by_css_selector("a.a-put-app > span.app-top-navbar-desc").click()
  
  def assert_application_present(self,application_name):
    driver = selenium_driver.driver
    app_list = driver.find_elements_by_class_name('a-name-a')
    index = 0
    for app in app_list:
      if(app.text == application_name):
        index =1
    if(index == 0):
      raise Exception("Application is not added successfully !")

  def edit_application(self,application_name):
    driver = selenium_driver.driver
    app_list = driver.find_elements_by_class_name('a-name-a')
    index = 0
    for app in app_list:
      if(app.text == application_name):
        app.click()
        index =1
    if(index == 0):
      raise Exception("Application is not present !")
