from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest

class test_searchfilter_py(unittest.TestCase):
    
    def test_feature(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-web-security") 
        options.add_argument("--disable-gpu")
        options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:5173/")
        self.driver.set_window_size(1536, 816)
        self.driver.find_element(By.LINK_TEXT, "Sign up").click()
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("test3")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("test3@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("test3")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
  

if __name__ == '__main__':
    unittest.main()