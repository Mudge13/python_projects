from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

browser = webdriver.Chrome()

# browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
# browser.get('https://only-testing-blog.blogspot.com/')
# browser.get('https://www.techlistic.com/p/selenium-practice-form.html')

browser.maximize_window()

browser.get('https://only-testing-blog.blogspot.com/')

assert 'Only' in browser.title

button = browser.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
print(button.get_attribute('innerHTML'))
# print(button.text)

assert 'Double-Click Me To See Alert' in browser.page_source

user_msg = browser.find_element(By.NAME, 'gparent1')
user_msg.clear()
user_msg.send_keys("Grandma cookies")

# Create an ActionChains object for mouse actions
actions = ActionChains(browser)

# Perform a double-click action on the button
actions.double_click(button).perform()

# Switch to the alert
alert = Alert(browser)

# Accept the alert (click "OK")
alert.accept()

time.sleep(5)
