import os

import allure
from dotenv import load_dotenv

from yandex_market.pages.authorization import authorization
from yandex_market.pages.main_page import main_page

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


@allure.epic("starmain")
@allure.feature("coolfeature1")
@allure.story("yanmain1")
@allure.severity("hight")
@allure.suite("Действия в карточке продукта")
@allure.id("1")
def test_adding_item_in_wishlist():  # passed
    '''GIVEN'''
    authorization.successful_authorization(login, password)

    '''WHEN'''
    main_page.search_for_items()
    main_page.action.add_product_in_wishlist()

    '''THEN'''
    main_page.action.check_item_in_wishlist()


@allure.epic("starmain")
@allure.feature("coolfeature1")
@allure.story("yanmain1")
@allure.severity("hight")
@allure.suite("Действия в карточке продукта")
@allure.id("2")
def test_adding_item_in_basket():  # passed
    '''GIVEN'''
    authorization.successful_authorization(login, password)

    '''WHEN'''
    main_page.search_for_items()
    main_page.action.add_item_in_basket()

    '''THEN'''
    main_page.action.check_item_in_basket()


@allure.epic("starmain")
@allure.feature("coolfeature1")
@allure.story("yanmain1")
@allure.severity("hight")
@allure.suite("Действия в карточке продукта")
@allure.id("4")
def test_delete_item_from_basket():  # passed
    '''GIVEN'''
    authorization.successful_authorization(login, password)

    '''WHEN'''
    main_page.go_into_basket()
    main_page.action.check_item_in_basket()

    '''THEN'''
    main_page.action.delete_item_from_basket()


@allure.epic("starmain")
@allure.feature("coolfeature1")
@allure.story("yanmain1")
@allure.severity("hight")
@allure.suite("Действия в карточке продукта")
@allure.id("5")
def test_add_item_in_compare_list():  # passed
    '''GIVEN'''
    authorization.successful_authorization(login, password)

    '''WHEN'''
    main_page.search_for_items()
    main_page.action.add_item_in_compare_list()
    main_page.go_into_compare_list()

    '''THEN'''
    main_page.action.check_item_in_compare_list()


@allure.epic("starmain")
@allure.feature("coolfeature1")
@allure.story("yanmain1")
@allure.severity("hight")
@allure.suite("Действия в карточке продукта")
@allure.id("6")
def test_delete_item_from_compare_list():  # passed
    '''GIVEN'''
    authorization.successful_authorization(login, password)

    '''WHEN'''
    main_page.go_into_compare_list()
    main_page.action.check_item_in_compare_list()

    '''THEN'''
    main_page.action.delete_item_from_comapre_list()
