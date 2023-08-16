# Automated system testing of an e-commerce store 'Magento' - backend.

# Test case 5 (TC005) - product review.

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

# Test step 1 - go to the UI and submit a review for a product.

driver.switch_to.new_window()
driver.get('http://live.techpanda.org/index.php/')
driver.find_element(By.XPATH, '//*[@id="nav"]/ol/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/h2/a').click()
driver.find_element(By.XPATH, '//*[@id="product_addtocart_form"]/div[3]/div[3]/div/p/a[2]').click()
sleep(2)

driver.find_element(By.XPATH, '//*[@id="Quality 1_3"]').click()
driver.find_element(By.XPATH, '//*[@id="review_field"]').send_keys('Test review')
driver.find_element(By.XPATH, '//*[@id="summary_field"]').send_keys('Test review')
driver.find_element(By.XPATH, '//*[@id="nickname_field"]').send_keys('nickname123')
driver.find_element(By.XPATH, '//*[@id="review-form"]/div[2]/button').click()

# Test step 2 - in the admin panel, go to
# "Catalogue -> Reviews and Ratings -> Customer Reviews -> Pending Reviews Menu".

# Expected result - the new review is added to the database.

wnd = driver.window_handles
driver.switch_to.window(wnd[0])

driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li/a').click()
driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li/ul/li[1]/ul/li[1]/a').click()
sleep(2)

nick = driver.find_element(By.XPATH, '//*[@id="reviwGrid_table"]/tbody/tr[1]/td[5]').text
try:
    assert nick == 'nickname123'
    print('TC005 step 2: passed')
except AssertionError:
    print('TC005 step 2: failed')

# Test step 3 - change the status of the review to "Approved".

driver.find_element(By.XPATH, '//*[@id="reviwGrid_table"]/tbody/tr[1]/td[1]/input').click()
select = Select(driver.find_element(By.XPATH, '//*[@id="reviwGrid_massaction-select"]'))
select.select_by_visible_text('Update Status')
select = Select(driver.find_element(By.XPATH, '//*[@id="status"]'))
select.select_by_visible_text('Approved')
driver.find_element(By.XPATH, '//*[@title="Submit"]').click()

# Test step 4 - go back to the product page.

# Expected result - the review is visible in the UI.

wnd = driver.window_handles
driver.switch_to.window(wnd[1])
driver.refresh()
sleep(2)
driver.execute_script("window.scrollTo(0,300)")
driver.get_screenshot_as_file('TC005.png')

driver.close()
