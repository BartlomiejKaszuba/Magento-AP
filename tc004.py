# Automated system testing of an e-commerce store 'Magento' - backend.

# Test case 4 (TC004) - sorting the database.

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

# Test step 1 - go to "Sales -> Invoices".

driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/ul/li[2]/a').click()
sleep(3)

# Test step 2a - sort by date in ascending order.

# Expected result - the records are sorted.

driver.find_element(By.XPATH, '//*[@name="order_created_at"]').click()
sleep(2)
driver.get_screenshot_as_file('TC004-1.png')

# Test step 2b - sort by date in descending order.

# Expected result - the records are sorted.

driver.find_element(By.XPATH, '//*[@name="order_created_at"]').click()
sleep(2)
driver.get_screenshot_as_file('TC004-2.png')

driver.close()
