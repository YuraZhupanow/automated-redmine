import pytest
from selenium import webdriver
import logging


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    logging.info("Starting browser")
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser not supported: {browser}")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    logging.info("Browser closed")
