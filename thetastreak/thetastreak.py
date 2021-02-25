#!/usr/bin/env python
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

TG_USERNAME = os.environ.get("TG_USERNAME")
TG_PASSWORD = os.environ.get("TG_PASSWORD")

driver = webdriver.Chrome()
driver.get("https://thetagang.com/login")
assert "THETA GANG" in driver.title

elem = driver.find_element_by_id("Username")
elem.clear()
elem.send_keys(TG_USERNAME)

elem = driver.find_element_by_id("Password")
elem.clear()
elem.send_keys(TG_PASSWORD)

elem.send_keys(Keys.RETURN)
assert TG_USERNAME in driver.page_source
driver.close()
