# Automated system testing of an e-commerce store 'Magento' - backend.

# Test case 3 (TC003) - disabled fields in a customer record.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Preconditions:
# 1. The website http://live.techpanda.org/index.php/backendlogin/ is open.

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://live.techpanda.org/index.php/backendlogin/')

# 2. Logged in through backend login.

username = 'user01'
password = 'guru99com'

driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'login').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/input').click()
sleep(5)
driver.find_element(By.XPATH, '//*[@id="message-popup-window"]/div[1]/a').click()

# Test step 1 - open any customer's details.

driver.find_element(By.XPATH, '//*[@id="customerGrid_table"]/tbody/tr[1]').click()
sleep(3)

# Test step 2 - click on "Account Information".

# Expected result - "Associate to Website" and "Created From" controls are disabled. "New Password" field is blank.

# Unable to fulfill step 2 due to a critical bug (see Bug Report #03).

driver.close()
