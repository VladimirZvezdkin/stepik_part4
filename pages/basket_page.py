from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_not_products_in_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET)
        basket.click()
        assert self.is_not_element_present(By.CLASS_NAME, 'col-sm-6'), "The basket contains products!"

    def basket_is_empty(self):
        assert self.is_element_present(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]'), "The basket is not empty!"


