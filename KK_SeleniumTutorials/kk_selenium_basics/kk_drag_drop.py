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

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3. Create ActionChains object
actions = ActionChains(driver)
#actions.scroll_by_amount(0,190)

#4. drag and drop
drag = driver.find_element(By.ID,'draggable')
drop = driver.find_element(By.ID, 'droppable')

actions.drag_and_drop(drag,drop).perform()
time.sleep(10)