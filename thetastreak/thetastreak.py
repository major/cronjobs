#!/usr/bin/env python
"""Keep the theta streak alive! 🔥"""
import os

from playwright.sync_api import Playwright, sync_playwright

TG_USERNAME = os.environ.get("TG_USERNAME")
TG_PASSWORD = os.environ.get("TG_PASSWORD")


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://thetagang.com/login
    page.goto("https://thetagang.com/login")

    # Click text=RELEASE NOTES
    page.locator("text=RELEASE NOTES").click()

    # Press Escape
    page.locator('div[role="dialog"]').press("Escape")

    # Click [placeholder="username"]
    page.locator('[placeholder="username"]').click()

    # Fill [placeholder="username"]
    page.locator('[placeholder="username"]').fill(TG_USERNAME)

    # Click [placeholder="password"]
    page.locator('[placeholder="password"]').click()

    # Fill [placeholder="password"]
    page.locator('[placeholder="password"]').fill(TG_PASSWORD)

    # Click text=Sign In
    page.locator("text=Sign In").click()

    # Click text=Sign In
    # with page.expect_navigation(url="https://thetagang.com/"):
    with page.expect_navigation():
        page.locator("text=Sign In").click()

    # Click text=mhayden >> nth=1
    page.locator("text=mhayden").nth(1).click()
    # assert page.url == "https://thetagang.com/mhayden"

    # Click text=Open Trades
    page.locator("text=Open Trades").click()

    # Click img
    page.locator("img").click()
    # assert page.url == "https://thetagang.com/"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
