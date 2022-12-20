import time
import random
from selenium import webdriver

# Replace USERNAME and PASSWORD with your Instagram login credentials
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'

# Replace SEARCH_QUERY with the search query you want to use
SEARCH_QUERY = 'YOUR_SEARCH_QUERY'

# Replace COMMENT_TEXT with the text of the comment you want to leave
COMMENT_TEXT = 'This is an automated comment!'

# Set the path to the webdriver executable
DRIVER_PATH = '/path/to/webdriver'

# Create a webdriver object
driver = webdriver.Chrome(DRIVER_PATH)

# Navigate to the Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Wait for the page to load
time.sleep(2)

# Enter the login credentials
driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)

# Click the login button
driver.find_element_by_css_selector('button[type="submit"]').click()

# Wait for the page to load
time.sleep(2)

# Navigate to the search page
driver.get('https://www.instagram.com/explore/tags/' + SEARCH_QUERY + '/')

# Wait for the page to load
time.sleep(2)

# Click the first post in the search results
driver.find_element_by_css_selector('a[href*="/p/"]').click()

# Wait for the page to load
time.sleep(2)

# Click the comment button
driver.find_element_by_css_selector('button[aria-label="Comment"]').click()

# Wait for the comment field to appear
time.sleep(1)

# Enter the comment text
driver.find_element_by_css_selector('textarea[aria-label="Add a comment…"]').send_keys(COMMENT_TEXT)

# Click the post button
driver.find_element_by_css_selector('button[type="submit"]').click()

# Wait for the comment to be posted
time.sleep(1)

# Close the webdriver
driver.close()
