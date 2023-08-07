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

    # Click [placeholder="username"]
    page.locator('[placeholder="username"]').click()

    # Fill [placeholder="username"]
    page.locator('[placeholder="username"]').fill(TG_USERNAME)

    # Click [placeholder="password"]
    page.locator('[placeholder="password"]').click()

    # Fill [placeholder="password"]
    page.locator('[placeholder="password"]').fill(TG_PASSWORD)

    # Click login button
    page.get_by_role("button", name="Login").click()

    page.goto(f"https://thetagang.com/{TG_USERNAME}")
    page.reload()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
