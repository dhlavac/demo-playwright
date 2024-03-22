from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("new project")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("another one project")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_text("another one project").click()
    page.locator("li").filter(has_text="another one project").get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="All").click()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="Completed").click()
    page.get_by_role("link", name="Active").click()
    page.get_by_text("Mark all as complete").click()
    page.get_by_text("Mark all as complete").click()
    expect(page.get_by_text("new project")).to_be_visible()
    page.get_by_text("new project").click()
    expect(page.locator("body")).to_contain_text("new project")
    expect(page.get_by_role("heading")).to_contain_text("todos")
