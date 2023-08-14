# Automated system testing of an e-commerce store 'Magento' - backend.

# Test case 2 (TC002) - generating an invoice.

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
sleep(3)

# Test step 2 - search for orders with a status "Cancelled".

select = Select(driver.find_element(By.XPATH, '//*[@id="sales_order_grid_filter_status"]'))
select.select_by_visible_text('Canceled')
driver.find_element(By.XPATH, '//*[@title="Search"]').click()
sleep(3)

# Test step 3 - select the first result and "Print invoices".

# Expected result - an error message is displayed: "There are no printable documents related to selected orders".

driver.find_element(By.XPATH, '//*[@id="sales_order_grid_table"]/tbody/tr[1]/td[1]/input').click()
select = Select(driver.find_element(By.XPATH, '//*[@id="sales_order_grid_massaction-select"]'))
select.select_by_visible_text('Print Invoices')
driver.find_element(By.XPATH, '//*[@title="Submit"]').click()
sleep(3)

expected_message = "There are no printable documents related to selected orders."
actual_message = driver.find_element(By.XPATH, '//*[@id="messages"]/ul/li/ul/li').text
try:
    assert actual_message == expected_message
    print('TC002 step 3: passed')
except AssertionError:
    print('TC002 step 3: failed')

# Test step 4 - search for orders with a status "Complete".

select = Select(driver.find_element(By.XPATH, '//*[@id="sales_order_grid_filter_status"]'))
select.select_by_visible_text('Complete')
driver.find_element(By.XPATH, '//*[@title="Search"]').click()
sleep(3)

# Test step 5 - select the first result and "Print invoices".

# Expected result - the invoice is downloaded.

driver.find_element(By.XPATH, '//*[@id="sales_order_grid_table"]/tbody/tr[1]/td[1]/input').click()
select = Select(driver.find_element(By.XPATH, '//*[@id="sales_order_grid_massaction-select"]'))
select.select_by_visible_text('Print Invoices')
driver.find_element(By.XPATH, '//*[@title="Submit"]').click()
sleep(3)

driver.close()
