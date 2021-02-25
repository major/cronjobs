#!/usr/bin/env python
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

TG_USERNAME = os.environ.get("TG_USERNAME")
TG_PASSWORD = os.environ.get("TG_PASSWORD")

chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://thetagang.com/login")

time.sleep(5)

elem = driver.find_element_by_xpath('//*[@id="Username"]')
elem.clear()
elem.send_keys(TG_USERNAME)

elem = driver.find_element_by_xpath('//*[@id="Password"]')
elem.clear()
elem.send_keys(TG_PASSWORD)

elem.send_keys(Keys.RETURN)
assert TG_USERNAME in driver.page_source
driver.close()
