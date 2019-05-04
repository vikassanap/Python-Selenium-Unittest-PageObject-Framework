from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject


class AddNewTenantPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.assertEqual("Application :: Add Tenant", self.driver.title)

  def add_tenant(self,tenant_id,tenant_name,tenant_admin,admin_password,admin_password_renter,tenant_email,tenant_desc):
    driver = selenium_driver.driver
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.find_element_by_name("T").send_keys(tenant_id)
    driver.find_element_by_name('TN').send_keys(tenant_name)
    driver.find_element_by_name('U').send_keys(tenant_admin)
    driver.find_element_by_name('P1').send_keys(admin_password)
    driver.find_element_by_name('P2').send_keys(admin_password_renter)
    driver.find_element_by_name('TE').send_keys(tenant_email)
    driver.find_element_by_name('TD').send_keys(tenant_desc)
    driver.find_element_by_name('actionType').click()
    driver.switch_to.default_content()
  	



