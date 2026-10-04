import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Opens a fresh Chrome browser for each test and closes it afterwards."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Uncomment the next line to run without a visible browser window:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """If a test fails, save a screenshot into the 'screenshots' folder."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join("screenshots", f"{item.name}_{stamp}.png")
            driver.save_screenshot(path)
            print(f"\nScreenshot saved: {path}")