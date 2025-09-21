'''
Created on 05-Sept-2025

@author: ADMIN
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#3.XPATH for Mbps and MB's
'''//td[contains(text(),'Mbps')]
//td[contains(text(),'MB/s')]
//td[contains(text(), '%')]
//td[contains(text(),'MB') and not (contains(text(),'/s'))]'''

#Create ActionChains object
action = ActionChains(driver)

'''//tbody[@id="rows"]/tr[1]/td[1]'''





