'''
Created on 27-Aug-2025


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


#2. Navigate to practice site
driver.get("http://practice.automationtesting.in")

#3. Click to demo site
demo_site = driver.find_element(By.LINK_TEXT, "Demo Site")
demo_site.click()

#4.writing first name
first_name = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
first_name.send_keys("Kannada")

#5.writing last name
last_name = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')
last_name.send_keys("Kasturi")

#6.writing Address
address = driver.find_element(By.TAG_NAME, 'textarea')
address.send_keys("Mandya, Karnataka, India")

#7.writing email address
email = driver.find_element(By.XPATH, '//input[@type="email"]')
email.send_keys("kasturi2025@gmail.com")

#8.writing phone number
phone_number = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[4]/div/input')
phone_number.send_keys("6363323243")

#9.Select female radio button
female_radio_button = driver.find_element(By.XPATH, '//input[@value="FeMale"]')
female_radio_button.click() 

#10 Select Cricket checkbox
cricket_checkbox = driver.find_element(By.XPATH, '//input[@value="Cricket"]')
cricket_checkbox.click()

#11. Select Movies checkbox
movies_checkbox = driver.find_element(By.ID, 'checkbox2')
movies_checkbox.click()

#12. Select hockey checkbox
hockey_checkbox = driver.find_element(By.ID, 'checkbox3')
hockey_checkbox.click()

#13. Select language dropdown
language_dropdown = driver.find_element(By.ID, 'msdd')
language_dropdown.click()

#14. Select English language
english_language = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a')
english_language.click()

#15. come out of the language dropdown
driver.find_element(By.XPATH, '//label[text()="Languages"]').click()

#16. Select skills dropdown
skills_dropdown = driver.find_element(By.ID, 'Skills')
skills_dropdown.click()
time.sleep(2)

#17. Select Python from the skills dropdown
python_skill = driver.find_element(By.XPATH, '//*[@id="Skills"]')
python_skill.send_keys("Python")

#come out of the skills dropdown
driver.find_element(By.XPATH, '//label[text()="Skills"]').click()

#18. Select country dropdown
'''country_dropdown = driver.find_element(By.XPATH, '//*[@id="countries"]')
country_dropdown.click()
time.sleep(2)

#19 click on select country dropdown
select_country_dropdown = driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span')
select_country_dropdown.click()

#20. Select India from the select country dropdown
india_option = driver.find_element(By.XPATH, '//li[text()="India"]')
india_option.click()

#21. Select Date of Birth year, month and day
dob_year = driver.find_element(By.ID, 'yearbox')
dob_year.send_keys("2001")

#22. Select Date of Birth month
dob_month = driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
dob_month.send_keys("October")

#23. Select Date of Birth day
dob_day = driver.find_element(By.ID, 'daybox')
dob_day.send_keys("20")

#24. Set password and confirm password
password = driver.find_element(By.ID, 'firstpassword')
password.send_keys("Kastu12345@")

confirm_password = driver.find_element(By.ID, 'secondpassword')
confirm_password.send_keys("Kastu12345@")

#25. Click on submit button
submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_button.click()'''





