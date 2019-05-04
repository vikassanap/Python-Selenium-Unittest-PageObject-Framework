import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from main import *


class LoginTests(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.driver = selenium_driver.connect(config['login_url'],config['browser'],config['implicit_wait'])
    self.base_url = selenium_driver.base_url    

  def setUp(self):
    self.driver.get(self.base_url)
    self.driver.maximize_window()
 
  def tearDown(self):
    if sys.exc_info()[0]:
            base_test_object = BaseTestObject()
            base_test_object.take_screenshot(self.driver,self._testMethodName)
    self.driver.delete_all_cookies()

  @classmethod
  def tearDownClass(self):
    self.driver.close()

  def test_valid_login(self):
    login_page_object = LoginPageObject(self.driver, self.base_url)
    login_page_object.login_with(test_data['lt_username'],test_data['lt_password'])
    manage_server_page_object = ManageServerPageObject(self.driver, self.base_url)
    manage_server_page_object.assert_welcome_text(test_data['lt_userid'])

  def test_invalid_login(self):
    login_page_object = LoginPageObject(self.driver, self.base_url)
    login_page_object.login_with(test_data['lt_invalid_username'],test_data['lt_invalid_password'])
    login_page_object.assert_error_text(test_data['lt_login_error_text'])

def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(LoginTests))
  return suite

def smoke_suite():
  suiteFew = unittest.TestSuite()
  suiteFew.addTest(LoginTests("test_valid_login"))
  return suiteFew


if __name__ == "__main__":
    unittest.main()
