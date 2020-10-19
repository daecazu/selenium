#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Todas las pruebas están realizadas sobre
http://demo-store.seleniumacademy.com/

"""
import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver/chromedriver')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
    
    # search an element by the html tag ID 
    
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
    
    # search an element by the html tag name 
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
    
    # search an element by the html tag class name
    def test_search_text_field_class(self):
        search_field = self.driver.find_element_by_class_name("input-text")
    
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    # count promo banner images
    def test_count_images(self):
        banner_list =  self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath(' //*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)