from pageobjects.base import selenium_driver
from pageobjects.base.basepageobject import BasePageObject
 
class TenantsPageObject(BasePageObject):

  def __init__(self, driver, base_url):
    self.driver = driver
    self.assertEqual("Application :: :: Tenants", self.driver.title)
    self.add_icon = self.driver.find_element_by_class_name('a-new-user')

  def click_add_icon(self):
    self.add_icon.click()

  def tenant_added_success_message(self, tenant_name):
    driver = selenium_driver.driver
    info_box=driver.find_element_by_class_name('info-box')
    text_to_assert = "Tenant "+tenant_name+" was successfully added"
    assert info_box.text == text_to_assert

  def assert_tenants(self, tenant_id,tenant_name):
    driver = selenium_driver.driver
    tenant_value =  tenant_id +" ("+tenant_name+")"
    print tenant_value
    a= driver.find_element_by_class_name("a-list")
    tenant_list = a.find_elements_by_class_name("a-name")
    size_of_list = len(tenant_list)
    index = 0
    for tenant in tenant_list:
      if(tenant.text == tenant_value):
        index =1
    if(index == 0):
      raise Exception("Tenant is not added successfully !")
      
        


      


