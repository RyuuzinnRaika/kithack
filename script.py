# Selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://navi.mars.kanazawa-it.ac.jp/portal/student/')
time.sleep(5)
driver.quit()