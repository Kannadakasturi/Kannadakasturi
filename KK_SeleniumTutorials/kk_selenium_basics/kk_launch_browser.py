'''
Created on 15-Aug-2025

@author: ADMIN
'''

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

'''#3. Enter name
#Locate the name text box
name_txt_bx = driver.find_element(By.CSS_SELECTOR, '#name')
#name_txt_bx = driver.find_element(By.ID, 'name')

#Action
name_txt_bx.send_keys("Kannada Kasturi")

#4. Enter email
Email_txt_bx = driver.find_element(By.CSS_SELECTOR, '#email')
Email_txt_bx.send_keys("kannadakasturi1@gmail.com")

#5. Enter Phone number
Phone_number_txt_bx = driver.find_element(By.ID, 'phone')
Phone_number_txt_bx.send_keys("6362328243")

#6. Enter Address
text_area = driver.find_element(By.ID, 'textarea')
text_area.send_keys("Mandya, Karnataka, India")


#4. Click on male radio button
male_radio_button = driver.find_element(By.ID, "male")
male_radio_button.click()

#5. Click on Sunday checkbox

check_box = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in check_box:
    checkbox = driver.find_element(By.ID, day.lower())
    checkbox.click()
    
#12 Click on country dropdown
country_dropdown = driver.find_element(By.ID, "country")
country_dropdown.send_keys("India")

#13 Click on colors dropdown
colors_dropdown = driver.find_element(By.XPATH, '(//option[@value="red"])[1]')
colors_dropdown.click()

#14 Enter date picker 1
date_picker1 = driver.find_element(By.ID, "datepicker")
date_picker1.send_keys("15/08/2025")

#16 Enter date picker 3
date_picker3 = driver.find_element(By.ID, "start-date")
date_picker3.send_keys("25/08/2025")

#17 Enter date picker 4
date_picker4 = driver.find_element(By.ID, "end-date")
date_picker4.send_keys("30/08/2025")

#18 Click on submit button
submit_button = driver.find_element(By.XPATH, '//button[@onclick="calculateRange()"]')
submit_button.click()
time.sleep(4)

# locate the search button
search_button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
search_button.click()
time.sleep(2)

#Locate the search text box
search_txt_bx = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
search_txt_bx.send_keys("Selenium (software)")


# Locate the search button again after entering text
search_button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
search_button.click()

# Click on the search result link

result_link = driver.find_element(By.LINK_TEXT, "Selenium (software)")
result_link.click()
time.sleep(2)

#switch to the new window from selenium search result

#driver.switch_to.window(driver.window_handles[1])

print("======AFTER TAB SWITCH=======")
#print("driver.window_handles:", driver.window_handles)
print("driver.current_window_handle:", driver.current_window_handle)
print("title of the page:", driver.title)

window_handles = driver.window_handles
window_handles_list = list(window_handles)
driver.switch_to.window(window_handles_list[1])

result_link1 = driver.find_element(By.LINK_TEXT, "verification")
result_link1.click()     
time.sleep(2)                   

#switch back to the original window
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)'''








