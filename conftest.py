
import pytest
import os
from playwright.sync_api import sync_playwright
from utils.logger import get_logger
from utils.api_client import APIClient

logger = get_logger("browser")


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    headless_mode = os.getenv("CI") == "true"

    logger.info("Launching Chromium browser")

    browser = playwright_instance.chromium.launch(
        headless=headless_mode
    )

    yield browser

    logger.info("Closing Chromium browser")
    browser.close()


@pytest.fixture()
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()

    # Start recording browser activity
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield page

    # Check whether the test failed
    test_failed = (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    )

    if test_failed:

        # Create reports folder
        os.makedirs("reports", exist_ok=True)

        # Capture failure screenshot
        page.screenshot(
            path=f"reports/{request.node.name}.png"
        )

        # Save trace recording
        context.tracing.stop(
            path=f"reports/{request.node.name}-trace.zip"
        )

    else:
        # Stop recording without saving successful traces
        context.tracing.stop()

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


@pytest.fixture(scope="session")
def api_client(api_request_context):
    return APIClient(api_request_context)
