import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    status = "passed" if report.passed else "failed" if report.failed else "skipped"
    screenshot_name = f"{item.name}_{status}_screenshot"

    allure.attach(
        driver.get_screenshot_as_png(),
        name=screenshot_name,
        attachment_type=allure.attachment_type.PNG,
    )
