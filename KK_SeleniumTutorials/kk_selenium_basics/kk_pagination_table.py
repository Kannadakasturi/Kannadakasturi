'''
Created on 06-Sept-2025

@author: ADMIN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3. Creating ActionChains Object
action = ActionChains(driver)

#Clicking 1st page below Pagination web table
first_page = driver.find_element(By.XPATH,'//ul[@id="pagination"]/li[1]')
first_page.click()




        
            
        


 


