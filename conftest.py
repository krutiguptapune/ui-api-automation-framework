import pytest
import os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    headless_mode = os.getenv("CI") == "true"

    browser = playwright_instance.chromium.launch(
        headless=headless_mode
    )

    yield browser

    browser.close()

@pytest.fixture()
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()

    yield page

    # Check whether the test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        # Create reports folder if it doesn't exist
        os.makedirs("reports", exist_ok=True)

        # Capture screenshot
        screenshot_path = f"reports/{request.node.name}.png"

        page.screenshot(path=screenshot_path)

    context.close()

@pytest.fixture(scope="session")
def api_request_context(playwright_instance):
    request_context = playwright_instance.request.new_context()

    yield request_context

    request_context.dispose()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        item.rep_call = report