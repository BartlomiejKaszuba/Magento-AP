# Automated system testing of an e-commerce store 'Magento' - backend.

# Test case 1 (TC001) - exporting all orders in CSV.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

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

# Test step 1 - go to "Sales -> Orders".

driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="nav"]/li[1]/ul/li[1]/a').click()

# Test step 2 - select "CSV" in "Export to" dropdown menu.

# Expected result - the CSV file is downloaded.

sleep(5)
driver.find_element(By.XPATH, '//*[@title="Export"]').click()

driver.close()
