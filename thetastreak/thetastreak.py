#!/usr/bin/env python
import os

from playwright.sync_api import Playwright, sync_playwright

TG_USERNAME = os.environ.get("TG_USERNAME")
TG_PASSWORD = os.environ.get("TG_PASSWORD")


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://thetagang.com/
    page.goto("https://thetagang.com/")

    # Click text=Login
    page.locator("text=Login").click()
    # assert page.url == "https://thetagang.com/login"

    # Click [placeholder="username"]
    page.locator('[placeholder="username"]').click()

    # Fill [placeholder="username"]
    page.locator('[placeholder="username"]').fill(TG_USERNAME)

    # Press Tab
    page.locator('[placeholder="username"]').press("Tab")

    # Fill [placeholder="password"]
    page.locator('[placeholder="password"]').fill(TG_PASSWORD)

    # Click text=Sign In
    # with page.expect_navigation(url="https://thetagang.com/"):
    with page.expect_navigation():
        page.locator("text=Sign In").click()

    # Click text=mhayden >> nth=1
    page.locator("text=mhayden").nth(1).click()
    # assert page.url == "https://thetagang.com/mhayden"

    # Click text=Open Trades
    # with page.expect_navigation(url="https://thetagang.com/mhayden"):
    with page.expect_navigation():
        page.locator("text=Open Trades").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
