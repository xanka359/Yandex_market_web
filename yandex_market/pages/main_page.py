from selene import browser, have, by
from selene.support.shared.jquery_style import s
from selenium.webdriver.remote import switch_to


class YandexMarketMainPage:

    def open(self):
        browser.open('/')
        return self

    def search_for_items(self):
        s('#header-search').click().type('грокаем алгоритмы')
        s('._1l7tY').element('._2bsQ5').should(have.text('Найти')).click()
        s('[data-auto="searchOrganic"]').element('.m4M-1').should(have.text('Грокаем алгоритмы'))
        return self

    def go_into_wishlist(self):
        s('.P23Bo').element('[href="/my/wishlist?track=head"]').click()
        return self

    def go_into_basket(self):
        s('#CART_ENTRY_POINT_ANCHOR').element('[href="/my/cart"]').click()
        return self

    def go_into_compare_list(self):
        s('#USER_MENU_ANCHOR').click()
        s('._3WotU').element('[href="/compare?track=menu"]').click()
        return self

    def drop_into_product_card(self):  #переиспользовать в методах
        s('[data-auto="searchOrganic"]').element('.m4M-1').should(have.text('Грокаем алгоритмы')).click()
        browser.switch_to_next_tab()
        s('[data-apiary-widget-id="/content/page/fancyPage/productTitle"]').should(have.text('Грокаем алгоритмы'))

    class ActionWithProductItem:
        def add_product_in_wishlist(self):
            main_page.drop_into_product_card()
            s('#wishlist').click()
            return self

        def check_item_in_wishlist(self):
            s('._32QL9').element('[href="/my/wishlist?track=head"]').click()
            s('.m4M-1').should(have.text('Грокаем алгоритмы'))
            return self

        def delete_item_from_wishlist(self):
            s('._2VECW').click().with_(timeout=10).element(by.text('Добавить в избранное')) #добавить таймаут до момента нотификации
            browser.config.timeout = 10
            #s('._2VECW').click()
            #s('._2VECW').should(have.text('Добавить в избранное'))
            #s('._3RJHd _2rQlS').should(have.text('Товар удалён из избранного'))#._3RJHd _2rQlS, <div data-auto="notification" class="_3HQti _2i0Mt _8WHWl top cia-vs" data-zone-data="{&quot;type&quot;:&quot;info&quot;,&quot;message&quot;:&quot;Товар удалён из избранного&quot;,&quot;pageId&quot;:&quot;market:wishlist&quot;}" data-zone-name="notification"><div class="_3RJHd _2rQlS" tabindex="0" role="button">Товар удалён из избранного</div></div>
            browser.driver.refresh()
            s('._2rdbx _2SUA6 _33utW IFARr _1A5yJ').should(have.text('Сохраняйте здесь товары'))
            return self


        def add_item_in_basket(self):
            main_page.drop_into_product_card()
            s('._30YNL').click()
            return self

        def check_item_in_basket(self):
            browser.config.timeout = 50
            s('[href="/my/cart"]').click()
            s('._1eJOk').element('.EQlfk').should(have.text('Грокаем алгоритмы'))
            return self

        def delete_item_from_basket(self):
            s('._1AwVK').click()
            browser.driver.refresh()
            s('._23gJ9').should(have.text('Сложите в корзину нужные товары'))
            return self

        def add_item_in_compare_list(self):
            main_page.drop_into_product_card()
            s('._63Rdu').click()
            return self


        def check_item_in_compare_list(self):
            s('._2itQJ').should(have.text('Сравнение товаров'))
            s('.zvRJM').should(have.text('Грокаем алгоритмы')) #.element('._3aQCh PzFNv cia-cs')
            return self

        def delete_item_from_comapre_list(self):
            s(by.text('Удалить список')).click() #.should(have.text('Удалить список'))
            s('.kpCeE').element('._2szVR').should(have.text('Сравнивать пока нечего'))

    action = ActionWithProductItem()


main_page = YandexMarketMainPage()
