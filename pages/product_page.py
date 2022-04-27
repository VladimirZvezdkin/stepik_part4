from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def view_basket(self):
        view_basket_button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        view_basket_button.click()

    def is_book_added_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert book_name == message, 'The added to basket book is wrong!'

    def is_the_price_correct(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert book_price == basket_total, "The price is not correct!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear"


