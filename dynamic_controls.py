import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver/chromedriver')
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Dynamic Controls').click()
    
    def test_dynamic_controls(self):
        # enable /disable checkbox
        driver = self.driver

        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]") 
        checkbox.click()
        
        btn_checkbox = driver.find_element_by_css_selector("#checkbox-example > button")
        btn_checkbox.click()
        
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#checkbox-example > button")
                )
            )
        btn_checkbox.click()

        # enable disable btn

        btn_field = driver.find_element_by_css_selector("#input-example > button")
        btn_field.click()
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#input-example > input[type=text]")
                )
            )
        input_text = driver.find_element_by_css_selector("#input-example > input[type=text]")
        input_text.send_keys('test')
        btn_field.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)