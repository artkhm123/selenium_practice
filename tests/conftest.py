
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="yandex")
    parser.addoption(
        "--headless", action = "store_true")

@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None
    if _browser == "chrome":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome
        driver = webdriver.Chrome(options=options,
                                  executable_path="Users\khomiakov_a\Desktop\Python\drivers\chromedriver\chromedriver.exe")
    elif _browser == "ff" or _browser == "firefox":
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(
            options=options,
            executable_path="Users\khomiakov_a\Desktop\Python\drivers\geckodriver\geckodriver.exe",
        )
    elif _browser == "yandex":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(
            options=options,
            executable_path="Users\khomiakov_a\Desktop\Python\drivers\yandexdriver\yandexdriver.exe",
        )
    yield driver
    driver.close()