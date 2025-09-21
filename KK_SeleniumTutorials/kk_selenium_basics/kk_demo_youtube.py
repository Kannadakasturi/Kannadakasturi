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

#Creating action
action = ActionChains(driver)

#3. Mouse hover on video
video = driver.find_element(By.XPATH,"//a[text()='Video']")
action.move_to_element(video).perform()

#4. Mouse hover on youtube
youtube = driver.find_element(By.XPATH, "//a[text()='Youtube']")
action.move_to_element(youtube).click().perform()

