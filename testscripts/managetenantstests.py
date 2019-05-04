import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from main import *

class ManageTenantsTests(unittest.TestCase):
  def setUp(self):
    self.driver = selenium_driver.connect(config['login_url'],config['browser'],config['implicit_wait'])
    self.base_url = selenium_driver.base_url
    self.driver.get(self.base_url)
    self.driver.maximize_window()
 
  def tearDown(self):
    if sys.exc_info()[0]:
            base_test_object = BaseTestObject()
            base_test_object.take_screenshot(self.driver,self._testMethodName)
    self.driver.quit()

  def test_add_tenant(self):
    login_page_object = LoginPageObject(self.driver, self.base_url)
    login_page_object.login_with(test_data['mtt_username'],test_data['mtt_password'])
    manage_server_page_object = ManageServerPageObject(self.driver, self.base_url)
    manage_server_page_object.click_manage_tenants()
    tenants_page_object = TenantsPageObject(self.driver, self.base_url)
    tenants_page_object.click_add_icon()
    add_new_tenant_page_object = AddNewTenantPageObject(self.driver,self.base_url)
    add_new_tenant_page_object.add_tenant(test_data['tenant_id'],test_data['tenant_name'],test_data['tenant_admin'],test_data['admin_password'],test_data['admin_password_renter'],test_data['tenant_email'],test_data['tenant_desc'])
    tenants_page_object.assert_tenants(test_data['tenant_id'],test_data['tenant_name'])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ManageTenantsTests))
    return suite


if __name__ == "__main__":
    unittest.main()
