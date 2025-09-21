'''
Created on 02-Sept-2025

@author: ADMIN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#Create ActionChains object
actions = ActionChains(driver)

actions.scroll_by_amount(0,1200).perform()
time.sleep(11)



#3. copy text from field1

#cntrl+a
field1 = driver.find_element(By.ID, 'field1')
actions.key_down(Keys.CONTROL, field1).send_keys('a').key_up(Keys.CONTROL).perform()

#cntrl+c
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()


#4. Paste the text into field2 using keyboard actions
field2 = driver.find_element(By.ID,'field2') 
actions.key_down(Keys.CONTROL, field2).send_keys('v').key_up(Keys.CONTROL).perform()










