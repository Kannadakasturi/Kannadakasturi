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

#2.Navigate to a practice site
driver.get("https://demo.automationtesting.in/Frames.html")

#3. Switch to single iframe
driver.switch_to.frame("singleframe")

#3. Enter text in the single iframe
single_iframe = driver.find_element(By.TAG_NAME, 'input')
single_iframe.send_keys("Kannada")
time.sleep(2)

#4. Switch back to the main content
driver.switch_to.default_content()


#5. Click on iframe with in an iframe link
iframe_within_iframe_link = driver.find_element(By.XPATH, '//a[@href="#Multiple"]')
iframe_within_iframe_link.click()

time.sleep(2)

#6. Switch to outer iframe
outer_iframe = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_iframe)
time.sleep(1)


#7. Switch to inner iframe
inner_iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(inner_iframe)
time.sleep(1)

#8. Enter text in the inner iframe
inner_iframe_textbox = driver.find_element(By.TAG_NAME, 'input')
inner_iframe_textbox.send_keys("Kasturi")
time.sleep(1)

#9. Switch back to the main content
driver.switch_to.default_content()
time.sleep(1)



