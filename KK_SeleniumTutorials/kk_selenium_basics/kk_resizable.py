'''
Created on 02-Sept-2025

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

driver.get("https://demo.automationtesting.in/Resizable.html")

#Create ActionChains object
actions = ActionChains(driver)

#3. Resize that box
resize_btn = driver.find_element(By.XPATH,'//*[@id="resizable"]/div[3]')
actions.click_and_hold(resize_btn).move_by_offset(130,100).release().perform()




