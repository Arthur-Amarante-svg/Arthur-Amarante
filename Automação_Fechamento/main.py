from selenium import webdriver
import time


# 1. Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# 2. Navigate to a web page
driver.get("https://archive.org/")

driver.find_element("id", "text-input").send_keys

time.sleep(15)