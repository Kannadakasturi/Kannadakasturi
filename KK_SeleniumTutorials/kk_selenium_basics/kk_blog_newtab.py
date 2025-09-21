'''
Created on 02-Sept-2025

@author: ADMIN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#create actions
action = ActionChains(driver)


#3. Mouse hover on Blog
blog = driver.find_element(By.LINK_TEXT,"Blog")
action.move_to_element(blog).perform()

#cntrl and click on blog
action.key_down(Keys.CONTROL).click(blog).key_up(Keys.CONTROL).perform()

#Go to new tab
driver.switch_to.window(driver.window_handles[1])

