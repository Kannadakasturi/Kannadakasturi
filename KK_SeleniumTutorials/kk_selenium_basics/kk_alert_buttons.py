'''
Created on 31-Aug-2025

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

#click on simple alert button
simple_alert_button = driver.find_element(By.ID,"alertBtn")
simple_alert_button.click()
time.sleep(2)

#click on ok button in the alert
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(2)

#click on prompt alert button
prompt_alert_button = driver.find_element(By.CSS_SELECTOR,"#confirmBtn")
prompt_alert_button.click()

#click on ok button in the prompt alert
prompt_alert = driver.switch_to.alert
prompt_alert.accept()

#click on confirmation alert button
confirmation_alert_button = driver.find_element(By.ID,"confirmBtn")
confirmation_alert_button.click()
time.sleep(1)

#click on cancel button in the confirmation alert
confirmation_alert = driver.switch_to.alert
confirmation_alert.dismiss()
time.sleep(1)

#click on prompt alert button
prompt_alert_button = driver.find_element(By.CSS_SELECTOR,"#promptBtn")
prompt_alert_button.click()
time.sleep(1)

#enter text in the prompt alert text box
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Kasturi")
prompt_alert.accept()