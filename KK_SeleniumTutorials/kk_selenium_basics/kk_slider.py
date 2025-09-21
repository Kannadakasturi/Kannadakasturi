'''
Created on 03-Sept-2025

@author: ADMIN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.action_chains import ActionChains

#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#Create ActionChains Object
actions = ActionChains(driver)

#3. Locate left slider
left_slider_btn = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
right_slider_btn = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')

#Action
actions.click_and_hold(left_slider_btn).move_by_offset(100,0).release().perform()

actions.click_and_hold(right_slider_btn).move_by_offset(100,0).release().perform()
