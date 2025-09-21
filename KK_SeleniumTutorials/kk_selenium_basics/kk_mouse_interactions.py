'''
Created on 02-Sept-2025

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

driver.get("https://demo.automationtesting.in/Resizable.html")

#Create ActionChains object
actions = ActionChains(driver)

#3. Mouse hover to interactions
interactions = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[6]/a') 
actions.move_to_element(interactions).perform()
time.sleep(2)

#4. drag nd drop
drag_drop_btn = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/a')
actions.move_to_element(drag_drop_btn).perform()

#5. click on static button
static_btn = driver.find_element(By.LINK_TEXT, 'Static')
actions.move_to_element(static_btn).perform()

actions.click(static_btn).perform()
