from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject
 
class LoginPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.wait_for_element_displayed_by_id(self.driver, "username")
    self.assertEqual("Application :: Login", self.driver.title)
    self.submit = self.driver.find_element_by_name("lAction")
    self.username = self.driver.find_element_by_id('username')
    self.password =self.driver.find_element_by_id('password')

  def click_submit(self):
    self.submit.click()

  def assert_error_text(self,val):
    driver = selenium_driver.driver
    error_text_element = driver.find_element_by_xpath(".//*[@id='center-content']/div[2]/form/div/div[1]/div/span")
    assert error_text_element.text == val

  def login_with(self,username,password):
    self.username.send_keys(username)
    self.password.send_keys(password)
    self.click_submit()