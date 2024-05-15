import os

import allure
from dotenv import load_dotenv

from yandex_market.pages.authorization import authorization

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


@allure.epic("starmain")
@allure.feature("coolfeature2")
@allure.story("yanmain2")
@allure.severity("blocker")
@allure.suite("Авторизация пользователя")
@allure.id("7")
def test_successful_authorization():
    '''GIVEN'''
    authorization.open()

    '''WHEN'''
    authorization.open_login_page()
    authorization.fill_login_form_valid_credentials(login=login, password=password)

    '''THEN'''
    authorization.check_authorized_info()


@allure.epic("starmain")
@allure.feature("coolfeature2")
@allure.story("yanmain2")
@allure.severity("blocker")
@allure.suite("Авторизация пользователя")
@allure.id("8")
def test_unsuccessful_authorization():
    '''GIVEN'''
    authorization.open()

    '''WHEN'''
    authorization.open_login_page()
    authorization.fill_login_form_invalid_credentials()

    '''THEN'''
    authorization.check_error_for_invalid_credentials()
