from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://thetagang.com/login")
    page.get_by_placeholder("username", exact=True).click()
    page.get_by_placeholder("username", exact=True).fill("major")
    page.get_by_placeholder("username", exact=True).press("Tab")
    page.get_by_placeholder("password").fill("7*n!KEiwpwecF65&G37p")
    page.get_by_role("button", name="Login").click()
    page.locator("#header i").click()
    page.locator("[id=\"C\"]").get_by_text("The Lab 🧪").click()
    page.get_by_text("Home").click()
    page.get_by_text("major").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
