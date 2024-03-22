from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://test.dolbite.com/")
    page.get_by_role("link", name="Login").click()
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("test@example.com")
    page.locator("input[name=\"email\"]").press("Tab")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("password")
    page.get_by_role("button", name="Log in").click()
    expect(page.locator("h1")).to_contain_text("I would like to learn...")
