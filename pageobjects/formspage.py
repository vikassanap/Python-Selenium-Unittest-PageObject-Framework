from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject

class FormsPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.assertEqual("Application :: Forms", self.driver.title)

  def edit_form(self,form_name):
    pass
  
  def save_form(self):
    pass

  def test_form(self):
    pass

  def drag_control(self):
    pass