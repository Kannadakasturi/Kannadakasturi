'''
Created on 17-Sept-2025

@author: ADMIN
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOrangeHRMLoginPage(unittest.TestCase):


    def test_navigation_to_orangehrm_login_page(self):
        #1. Launch the Chrome browser with desired capabilities

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(2)

        #2. Navigate to a practice site
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        #3. Validating the page title
        expected_title = "OrangeHRM"
        actual_title = driver.title
        self.assertEqual(actual_title, expected_title, "Page title is not matched")
        
        #4.Validating the page url
        expected_url_portion = "/auth/login"
        actual_url = driver.current_url
        self.assertIn(expected_url_portion, actual_url, "Current page url doesnot contain '/auth/login'")
        
    def test_orangehrm_login(self):
        #1. Launch the Chrome browser with desired capabilities

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(2)

        #2. Navigate to a practice site
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        #3. Enter User name
        user_name_txt_bx = driver.find_element(By.NAME,'username')
        user_name_txt_bx.send_keys("Admin")
        
        #4. Enter Password
        password_txt_bx = driver.find_element(By.NAME,"password")
        password_txt_bx.send_keys("admin123")
        
        #5. Click on login btn
        login_btn = driver.find_element(By.XPATH,"//button[@type='submit']")
        login_btn.click()
        
        #6. Validate the successful login
        expected_url_portion = "/dashboard/index"
        actual_url = driver.current_url
        self.assertIn(expected_url_portion, actual_url, "login is failed")
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()