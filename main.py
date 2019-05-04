import unittest
from pageobjects.base import selenium_driver
from pageobjects.login import LoginPageObject
from pageobjects.manageserver import ManageServerPageObject
from pageobjects.tenants import TenantsPageObject
from pageobjects.addnewtenant import AddNewTenantPageObject
from pageobjects.base.basetestobject import BaseTestObject
from pageobjects.myapplications import MyApplicationsPageObject
from pageobjects.uploadapplication import UploadApplicationPageObject
from pageobjects.formspage import FormsPageObject
from selenium.webdriver.common.action_chains import ActionChains
import yaml
import time
import xmlrunner
from datetime import datetime
from runner import HTMLTestRunner
import os

path =  os.path.dirname(os.path.realpath(__file__))
config_path = path+"/testdata/config.yml"

test_data_path = path+"/testdata/test_data.yml"

with open(test_data_path, 'r') as f:
    test_data = yaml.load(f)

with open(config_path, 'r') as f:
    config = yaml.load(f)