from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject

class ManageServerPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.assertEqual("Application :: :: Manage", self.driver.title)
    self.manage_tenant_link = self.driver.find_element_by_link_text("Manage Tenants")

  def click_manage_tenants(self):
    self.manage_tenant_link.click()

  def assert_welcome_text(self,val):
    driver = selenium_driver.driver
    welcome_text_element = driver.find_element_by_xpath(".//*[@id='header-top-navbar']/li[5]/span")
    welcome_text = "welcome "+val;
    assert welcome_text_element.text == welcome_text