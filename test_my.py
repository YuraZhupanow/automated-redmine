from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.goapr.com/')
element = browser.find_element(By.CLASS_NAME, 'filterPlatform')

