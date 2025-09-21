'''
Created on 07-Sept-2025

@author: ADMIN
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.shadowroot import ShadowRoot

#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")


#3. Locate the shadow host
shadow_host = driver.find_element(By.ID,'shadow_host')

#4. Get the shadow root
first_shadow_root = shadow_host.shadow_root


#4. Locate the element in shadow DOM using shadow root
shadow_input_textbox = first_shadow_root.find_element(By.CSS_SELECTOR, "input[type='text']")
shadow_input_textbox.send_keys("kasturi")

#5. Click on Blog below checkbox
check_box = first_shadow_root.find_element(By.CSS_SELECTOR,"input[type='checkbox']:nth-child(7)")
check_box.click()

#6. Get 'Mobiles' text
span = first_shadow_root.find_element(By.CSS_SELECTOR,'#shadow_content > span')
print(span.text)