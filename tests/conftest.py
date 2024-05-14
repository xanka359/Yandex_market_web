import os
from datetime import datetime
import allure
from selenium.webdriver.firefox.options import Options as FirefoxOptions
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

    # Добавляем куки в текущий сеанс браузера
    # cookies = {
    #     'visits': '1714943020-1714943020-1714943020',
    #     'cmp-merge': 'true',
    #     'reviews-merge': 'true',
    #     'oq_shown_onboardings': '%5B%5D',
    #     'oq_last_shown_date': '1714943020309',
    #     'rcrr': 'true',
    #     'muid': '1152921511014219385%3A4NeHeaNYTl97KPpQKKOv%2FJuDMDZrLIgw',
    #     'global_delivery_point_skeleton': '{"regionName":"Пенза","addressLineWidth":39.734375}',
    #     'parent_reqid_seq': '1714943020222%2F8e2be7d8e81afdcab0c88749bb170600%2F1%2F1,1714943022269%2Fe28b6f1f17453de47904a749bb170600%2F1%2F1',
    #     'server_request_id_market:index': '1714943022269%2Fe28b6f1f17453de47904a749bb170600%2F1%2F1',
    #     'ugcp': '1',
    #     'suppress_order_notifications': '1',
    #     'spvuid_market:index_3751af_expired:1715029424061': '1714943022269%2Fe28b6f1f17453de47904a749bb170600%2F1%2F1',
    #     'yashr': '5495545691714943039',
    #     'receive-cookie-deprecation': '1',
    #     'i': 'reHLq9ltaG8WA9YxB20YPRfwK9mFMKQeudqS2dLzXQkrRaC3idvfJ1FvoyFMnCu30nQTtAj15s9gAJolL6RuwiaIeJs=',
    #     'yandexuid': '4584957841714943039',
    #     'yuidss': '4584957841714943039',
    #     'ymex': '2030303039.yrts.1714943039',
    #     'gdpr': '0',
    #     '_ym_uid': '1714501318398004992',
    #     '_ym_d': '1714943042',
    #     'bh': 'Ej8iQ2hyb21pdW0iO3Y9IjEyNCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNCIsIk5vdC1BLkJyYW5kIjt2PSI5OSIaBSJ4ODYiIg8iMTI0LjAuNjM2Ny45MSIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUloiQ2hyb21pdW0iO3Y9IjEyNC4wLjYzNjcuOTEiLCJHb29nbGUgQ2hyb21lIjt2PSIxMjQuMC42MzY3LjkxIiwiTm90LUEuQnJhbmQiO3Y9Ijk5LjAuMC4wIiI=',
    #     '_ym_visorc': 'b',
    #     '_yasc': '7L5I6UbD6wF2A9CWYZGL7sTiyVRVEYIwzTh4MYwFHUk/L//jD5VtreDgE/Ct0zBdsA==',
    #     'Session_id': '3:1714943087.5.0.1714943087014:FKS1Xg:3e.1.2:1|110995102.0.2.3:1714943087|3:10287525.850182.70m-XlEdIKjIjv2CXQzdzkwColM',
    #     'sessar': '1.1189.CiDPypwfDT1I0SdO8qPH98cc8-sM0ql9dRzyLb-QSvxM_g.4iWTR1t7kZCXZylvICDvldQFor9BORWJSrM5yYPBLt0',
    #     'sessionid2': '3:1714943087.5.0.1714943087014:FKS1Xg:3e.1.2:1|110995102.0.2.3:1714943087|3:10287525.850182.fakesign0000000000000000000',
    #     'yp': '2030303087.udn.cDphbmRyb3ZhMjAxMg%3D%3D',
    #     'L': 'Q3BldghCA3VNelMDQQ5hXVRhRUVEblF0BgEGQSlEMnZ4cGU=.1714943087.15714.339915.368a11bc9311977afffcf5f8b92b4dd4',
    #     'yandex_login': 'androva2012',
    #     'ys': 'udn.cDphbmRyb3ZhMjAxMg%3D%3D#c_chck.1645658767'
    # }
    #
    # cookie_info = {
    #     'name': '_yasc',
    #     'value': 'slR1GpWxiX8T9bbcmrEvnHwsWUrh5pG4nR4MA6S59qmFXBKr7hdBUNxXpzQ90EA0bBLG',
    #     'domain': 'market.yandex.ru',
    #     'path': '/',
    #     'expiry': datetime(2034, 5, 3, 21, 4, 48),
    #     'secure': True
    # }
    #
    # expiry_str = cookie_info['expiry'].strftime('%a, %d %b %Y %H:%M:%S GMT')
    #
    # # Заменяем объект datetime строкой в cookie_info
    # cookie_info['expiry'] = expiry_str
    #
    # # Добавляем куки в браузер
    # browser.driver.add_cookie(cookie_info)

    #browser.config.browser_name = 'firefox'


    yield
    browser.quit()