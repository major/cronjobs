#!/usr/bin/env python
import logging
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

logging.info("Loading the site...")
driver.get("https://thetagang.com/login")

time.sleep(5)

elem = driver.find_element_by_xpath('//*[@id="Username"]')
elem.clear()
elem.send_keys(TG_USERNAME)

elem = driver.find_element_by_xpath('//*[@id="Password"]')
elem.clear()
elem.send_keys(TG_PASSWORD)

logging.info("Submitting login...")
elem.send_keys(Keys.RETURN)

time.sleep(5)

assert TG_USERNAME in driver.page_source

logging.info("Refresh the page...")
driver.refresh()

time.sleep(1)
driver.close()
logging.info("Done! 🎉")
