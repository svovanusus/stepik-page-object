from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_registration_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not presented!"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented!"


    def should_be_registration_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented!"


    def register_new_user(self, email: str, password: str):
        email_el: WebElement = None
        password_el: WebElement = None
        confirm_el: WebElement = None
        button_el: WebElement = None

        try:
            email_el = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        except NoSuchElementException:
            assert False, "Email field is not presented!"
        
        try:
            password_el = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        except NoSuchElementException:
            assert False, "Password field is not presented!"
        
        try:
            confirm_el = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM)
        except NoSuchElementException:
            assert False, "Confirm password field is not presented!"

        try:
            button_el = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        except NoSuchElementException:
            assert False, "Registration button is not presented!"

        email_el.send_keys(email)
        password_el.send_keys(password)
        confirm_el.send_keys(password)

        button_el.click()
