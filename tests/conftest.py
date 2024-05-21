import os
from utils import attach
from dotenv import load_dotenv
from selene import browser
import pytest


load_dotenv()
login = os.getenv('LOGIN_SELENOID')
password = os.getenv('PASSWORD_SELENOID')

URL = 'https://passport.yandex.ru'

@pytest.fixture(scope='function', autouse=True)
def manage_browser():
    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "100.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    # login_selenoid = os.getenv('login')
    # password_selenoid = os.getenv('password')
    #
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login_selenoid}:{password_selenoid}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )

    browser.config.base_url = 'https://market.yandex.ru/'
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.timeout = 6.0

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()