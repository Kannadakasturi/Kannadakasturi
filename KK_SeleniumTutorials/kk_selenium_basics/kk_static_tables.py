'''
Created on 05-Sept-2025

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

#3. Get learn_selenium from Static web table

'''table_cell = driver.find_element(By.XPATH,'//table[@name="BookTable"]/tbody/tr[2]/td[1]')
table_cell_value = table_cell.text
print(table_cell_value)

#get all texts from static web table

for i in range(3,8):
    for j in range(1,5):
        table_cells = driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{i}]/td[{j}]')
        table_cells_value = table_cells.text
        print(table_cells_value,end=" ")
    print()'''    

'''#Using length function take input as book name and print its price
rows = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]/tbody/tr'))
cols = len(driver.find_elements(By.XPATH,'//table[@name="BookName"]/tbody/tr/th'))
print(rows)
print(cols)
for i in range(1,rows+1):
    book = driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{i}]/*[1]').text
    price = driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{i}]/*[4]').text
    print(f'{book:<18}|{price}')'''
    
#take book name as i/p from the user and print its price

book_name = input("enter the book name:")
for i in range(2,8):
    table_cell = driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{i}]/td[1]')
    table_cell_value = table_cell.text
        
    if book_name == str(table_cell_value):
        table_cell_1 = driver.find_element(By.XPATH,f'//table[@name="BookTable"]/tbody/tr[{i}]/td[4]')
        table_price = table_cell_1.text  
        print(f"price of {book_name} is {table_price}")
    
    