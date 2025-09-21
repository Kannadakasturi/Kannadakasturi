'''
Created on 04-Sept-2025

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

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

#3. Create ActionChains object
actions = ActionChains(driver)

'''#4.right_click_me
right_click_btn = driver.find_element(By.XPATH, "//span[text()='right click me']")
actions.move_to_element(right_click_btn).click().perform()'''