from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BOOK_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    VIEW_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.col-sm-1 .align-right')
    BASKET_TOTAL = (By.CSS_SELECTOR, '#basket_totals .price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, 'span.btn-group')
