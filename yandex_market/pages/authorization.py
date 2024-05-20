import os

import allure
from dotenv import load_dotenv
from selene import browser, have, by, command
from selene.support.shared.jquery_style import s

load_dotenv()


class Authorization:
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    @allure.step('Открыть главную страницу ')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        s('#USER_MENU_ANCHOR').element(by.text('Войти')).click()
        s('[data-type="login"]').click()
        return self

    @allure.step('Заполнить логин и пароль корректными данными')
    def fill_login_form_valid_credentials(self, login, password):
        s('#passp-field-login').type(f'{login}')
        s('.passp-sign-in-button').should(have.text('Войти')).click()
        s('#passp-field-passwd').click().type(f'{password}')
        s('.passp-sign-in-button').should(have.text('Продолжить')).click()
        return self

    @allure.step('Проверить имя авторизованного пользователя')
    def check_authorized_info(self):
        s('#USER_MENU_ANCHOR').click()
        s('.Npykn').element('[data-auto="public-user-info"]').should(have.text('Ксения А.'))
        browser.element('.Npykn').perform(command.js.scroll_into_view)
        return self

    @allure.step('Заполнить логин и пароль некорректными данными ')
    def fill_login_form_invalid_credentials(self):
        s('#passp-field-login').type('someLogin')
        s('.passp-sign-in-button').should(have.text('Войти')).click()
        s('#passp-field-passwd').click().type('somePassword')
        s('.passp-sign-in-button').should(have.text('Продолжить')).click()

    @allure.step('Проверить ошибку авторизации')
    def check_error_for_invalid_credentials(self):
        s('.Field-inputWrapper').should(have.text('Неверный пароль'))

    def successful_authorization(self, login, password):
        (self
         .open()
         .open_login_page()
         .fill_login_form_valid_credentials(login, password)
         )


authorization = Authorization()
