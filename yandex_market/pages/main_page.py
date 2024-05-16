import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s


class YandexMarketMainPage:

    @allure.step('Открыть главную страницу ')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Произвести поиск по продукту')
    def search_for_items(self):
        s('#header-search').click().type('грокаем алгоритмы')
        s('._1l7tY').element('._2bsQ5').should(have.text('Найти')).click()
        s('[data-auto="searchOrganic"]').element('.m4M-1').should(have.text('Грокаем алгоритмы'))
        return self

    @allure.step('Перейти в Избранное')
    def go_into_wishlist(self):
        s('.P23Bo').element('[href="/my/wishlist?track=head"]').click()
        return self

    @allure.step('Перейти в Корзину')
    def go_into_basket(self):
        s('#CART_ENTRY_POINT_ANCHOR').element('[href="/my/cart"]').click()
        return self

    @allure.step('Перейти в Список сравнения')
    def go_into_compare_list(self):
        s('#USER_MENU_ANCHOR').click()
        s('._3WotU').element('[href="/compare?track=menu"]').click()
        return self

    @allure.step('Перейти в карточку продукта')
    def drop_into_product_card(self):
        s('[data-auto="searchOrganic"]').element('.m4M-1').should(have.text('Грокаем алгоритмы')).click()
        browser.switch_to_next_tab()
        s('[data-apiary-widget-id="/content/page/fancyPage/productTitle"]').should(have.text('Грокаем алгоритмы'))

    class ActionWithProductItem:
        @allure.step('Добавить продукт в Избранное')
        def add_product_in_wishlist(self):
            main_page.drop_into_product_card()
            s('#wishlist').click()
            return self

        @allure.step('Проверить что продукт отображается в избранном')
        def check_item_in_wishlist(self):
            s('._32QL9').element('[href="/my/wishlist?track=head"]').click()
            s('.m4M-1').should(have.text('Грокаем алгоритмы'))
            return self

        @allure.step('Добавить продукт в Корзину')
        def add_item_in_basket(self):
            main_page.drop_into_product_card()
            s('._30YNL').click()
            return self

        @allure.step('Проверить что продукт отображается в корзине')
        def check_item_in_basket(self):
            browser.config.timeout = 50
            s('[href="/my/cart"]').click()
            s('._1eJOk').element('.EQlfk').should(have.text('Грокаем алгоритмы'))
            return self

        @allure.step('Удалить продукт из корзины')
        def delete_item_from_basket(self):
            s('._1AwVK').click()
            browser.driver.refresh()
            s('._23gJ9').should(have.text('Сложите в корзину нужные товары'))
            return self

        @allure.step('Добавить продукт в Список сравнения')
        def add_item_in_compare_list(self):
            main_page.drop_into_product_card()
            s('._63Rdu').click()
            return self

        @allure.step('Проверить что продукт отображается в списке сравнения')
        def check_item_in_compare_list(self):
            s('._2itQJ').should(have.text('Сравнение товаров'))
            s('.zvRJM').should(have.text('Грокаем алгоритмы'))
            return self

        @allure.step('Удалить продукт из списка сравнения')
        def delete_item_from_comapre_list(self):
            s(by.text('Удалить список')).click()
            s('.kpCeE').element('._2szVR').should(have.text('Сравнивать пока нечего'))

    action = ActionWithProductItem()


main_page = YandexMarketMainPage()
