from selenium import webdriver

 
class SeleniumWrapper:
  _instance = None
 
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
    return cls._instance
 
  def connect(self, host,browser,wait_time=10):
    self.driver = None
    if browser == "chrome":
        self.driver = webdriver.Chrome()
    elif browser == "firefox":
        self.driver = webdriver.Firefox()
    elif browser == "headless":
        self.driver = webdriver.PhantomJS()
    self.driver.implicitly_wait(wait_time)
    self.base_url = host
    return self.driver