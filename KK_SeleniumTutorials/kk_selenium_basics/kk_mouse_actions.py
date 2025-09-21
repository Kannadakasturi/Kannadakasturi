'''
Created on 01-Sept-2025

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

#4. Scrolling
actions.scroll_by_amount(0,1000).perform()

#5. Mouse hover on point me
point_me_button = driver.find_element(By.CLASS_NAME, 'dropbtn')
actions.move_to_element(point_me_button).perform()

#6. Double click on Copy text button
copy_txt_btn = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
actions.double_click(copy_txt_btn).perform()


