
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

import unittest

class test_newpropertypost_py(unittest.TestCase):
    def test_feature(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-web-security") 
        options.add_argument("--disable-gpu")
        options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:5173/")
        self.driver.set_window_size(1536, 816)
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("test1")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("password")
        signin_button = WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/form/button')))

        signin_button.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Profile").click()
        self.driver.find_element(By.CSS_SELECTOR, ".title:nth-child(3) button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Jeet Residency")
        self.driver.find_element(By.ID, "price").send_keys("50000")
        self.driver.find_element(By.ID, "address").send_keys("Palaj, Gandhinagar")
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        self.driver.find_element(By.CSS_SELECTOR, "p").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Spacious, well maintained, luxorious property</p>'}", element)
        element = self.driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Spacious, well maintained, luxurious property</p>'}", element)
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys("Gandhinagar")
        self.driver.find_element(By.ID, "bedroom").send_keys("5")
        self.driver.find_element(By.ID, "bathroom").send_keys("3")
        self.driver.find_element(By.ID, "latitude").send_keys("72.3")
        self.driver.find_element(By.ID, "longitude").send_keys("29.7")
        self.driver.find_element(By.ID, "income").click()
        self.driver.find_element(By.ID, "size").click()
        self.driver.find_element(By.ID, "size").send_keys("700")
        self.driver.find_element(By.ID, "school").send_keys("2")
        self.driver.find_element(By.ID, "bus").send_keys("2")
        self.driver.find_element(By.ID, "restaurant").click()
        self.driver.find_element(By.ID, "restaurant").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, ".sendButton").click()
      

if __name__ == '__main__':
    unittest.main()

