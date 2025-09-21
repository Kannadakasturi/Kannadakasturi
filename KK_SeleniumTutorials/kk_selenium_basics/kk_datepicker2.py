from selenium import webdriver
from selenium.webdriver.common.by import By


#1. Launch the Chrome browser with desired capabilities

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)

#2. Navigate to a practice site

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#Locate datepicker2
datepicker2 = driver.find_element(By.ID,"txtDate")

'''#Remove readonly attribute from datepicker2
driver.execute_script("arguments[0].removeAttribute('readonly')",datepicker2)

#Enter date in datepicker2
datepicker2.send_keys("13/09/2025")
driver.execute_script
'''

#Enter date in datepicker2 using script
driver.execute_script("arguments[0].value = arguments[1];",datepicker2,"13/10/2024")