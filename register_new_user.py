import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver/chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        
        create_account_buttom = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_buttom.is_displayed() and create_account_buttom.is_enabled())
        create_account_buttom.click()

        self.assertEqual('Create New Customer Account', driver.title)
        First_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_addresss = driver.find_element_by_id('email_address')
        newsletter_suscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_btn = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(
            First_name.is_enabled()
            and last_name.is_enabled()
            and middle_name.is_enabled()
            and email_addresss.is_enabled()
            and newsletter_suscription.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and submit_btn.is_enabled()
        )
        
        First_name.send_keys('Test')
        last_name.send_keys('Test')
        middle_name.send_keys('Test')
        email_addresss.send_keys('Test@unitest.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        newsletter_suscription.click()
        driver.implicitly_wait(30)
        submit_btn.click()


        
        



    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)   
