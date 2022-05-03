from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # check if url is correct
        assert 'login' in self.browser.current_url, 'There is no login url!'

    def should_be_login_form(self):
        # check if login form exists
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'There is no login form!'

    def should_be_register_form(self):
        # check if registration form exists
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'There is no registration form!'

    def register_new_user(self, email, password):
        # method for new user registration
        email_window = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)  # find email filed
        email_window.send_keys(email)  # insert email
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_FIELD)  # find password field
        password1.send_keys(password)  # insert password
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_FIELD)  # find password confirmation field
        password2.send_keys(password)  # insert password
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)  # find 'register' button
        register_button.click()  # click on 'register' button - registration
