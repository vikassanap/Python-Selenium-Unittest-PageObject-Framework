import unittest
import time
from datetime import datetime
import os

class BaseTestObject():

    def take_screenshot(self,driver,testcase_title):
      path =  os.path.dirname(os.path.realpath(__file__))
      screenshots_path = path+"/../../test-reports/screenshots/"
      screenshots_file = screenshots_path + testcase_title + ".png"
      driver.get_screenshot_as_file(screenshots_file)

