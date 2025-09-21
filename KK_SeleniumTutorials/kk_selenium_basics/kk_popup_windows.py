'''
Created on 30-Aug-2025

@author: ADMIN


'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")



#click on new tab button
new_tab_button = driver.find_element(By.XPATH, '//button[@onclick="myFunction()"]')
new_tab_button.click()


#click original window
driver.switch_to.window(driver.window_handles[1])

#click on pop up window button
popup_window_button = driver.find_element(By.ID, 'PopUp')
popup_window_button.click()
time.sleep(5)

#switch to the new window
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

#close the popup window
driver.close()

#switch back to the original window
driver.switch_to.window(driver.window_handles[0])

#write field 2 in the iframe
field_2 = driver.find_element(By.ID, 'field2')
field_2.send_keys("Hello Kasturi")
