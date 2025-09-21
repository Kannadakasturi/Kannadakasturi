'''
Created on 31-Aug-2025

@author: ADMIN
'''

from selenium import webdriver
from selenium.webdriver.common.by import By


import time
from selenium.webdriver.support.select import Select

#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3. Locate the <select> tag element
country_dropdown = driver.find_element(By.ID, 'country')

#4. Create a Select class object
select_country = Select(country_dropdown)

#5. Use the Select class object to perform selection

# Method 1: Select country by value
select_country.select_by_value('uk')
time.sleep(2)


# Method 2: Select country by visible text
select_country.select_by_visible_text('Australia')
time.sleep(2)

#deselect the selected option
#select_country.deselect_by_visible_text("Australia")   --> Works only for multi-select dropdowns

# Method 3: Select country by index
select_country.select_by_index(4)  # Index starts from 0
time.sleep(2)

#6. get the color of the dropdown
red_color = driver.find_element(By.XPATH, '(//option[@value="red"])')
red_color.click()

second_red_color = driver.find_element(By.XPATH, '(//option[@value="red"])[2]')
second_red_color.click()
time.sleep(2)

click_cat = driver.find_element(By.XPATH, '//option[@value="cat"]')
click_cat.click()

click_dear = driver.find_element(By.XPATH, '//option[@value="deer"]')
click_dear.click()

time.sleep(2)





