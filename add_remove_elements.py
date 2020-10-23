import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver/chromedriver')
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com")
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add? '))
        elements_removed = int(input('How many elements will you remove? '))
        total_elements = elements_added - elements_removed
        add_btn = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)
        for i in range(elements_added):
            add_btn.click()
        for i in range(elements_removed):
            try:
                delete_btn = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_btn.click()
            except:
                print("you're trying to delete more elements than the existent")
                break
        
        if total_elements > 0:
            print(f"there are {total_elements} elements on screen")
        else:
            print("There 0 elements on screen")

        sleep(3)
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)