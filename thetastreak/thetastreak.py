#!/usr/bin/env python
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_load(driver):
    """Wait for the page to be fully loaded."""
    time.sleep(5)
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script(
            "return document.readyState === 'complete'"
        )
    )


logging.basicConfig(level=logging.INFO)

TG_USERNAME = os.environ.get("TG_USERNAME")
TG_PASSWORD = os.environ.get("TG_PASSWORD")

chrome_options = Options()
# chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)

logging.info("Loading the site...")
driver.get("https://thetagang.com/login")

wait_for_load(driver)

# Clear the modal.
driver.refresh()

wait_for_load(driver)

elem = driver.find_element_by_xpath('//*[@id="Username"]')
elem.clear()
elem.send_keys(TG_USERNAME)

elem = driver.find_element_by_xpath('//*[@id="Password"]')
elem.clear()
elem.send_keys(TG_PASSWORD)

logging.info("Submitting login...")
elem.send_keys(Keys.ENTER)

wait_for_load(driver)

logging.info("Refresh the page...")
driver.refresh()

wait_for_load(driver)

premium_div = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div/div/div[3]/div[1]/div[1]/div[3]/div/div[4]/div[2]'
)
print(premium_div.text)

driver.close()
logging.info("Done! 🎉")
