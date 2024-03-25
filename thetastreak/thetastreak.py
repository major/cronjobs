#!/usr/bin/env python
"""Keep the theta streak alive! 🔥"""
import os

from playwright.sync_api import Playwright, sync_playwright

TG_USERNAME = os.environ.get("TG_USERNAME")
TG_PASSWORD = os.environ.get("TG_PASSWORD")


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://thetagang.com/login")
    page.get_by_placeholder("username", exact=True).click()
    page.get_by_placeholder("username", exact=True).fill(TG_USERNAME)
    page.get_by_placeholder("username", exact=True).press("Tab")
    page.get_by_placeholder("password").fill(TG_PASSWORD)

    page.get_by_role("button", name="Login").click()
    page.get_by_text("major, the Ember").click()
    page.locator("[id=\"C\"]").get_by_text("The Lab 🧪").click()
    page.reload()
    page.close()

    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
