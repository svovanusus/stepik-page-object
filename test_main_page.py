from selenium.webdriver.remote.webdriver import WebDriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_ligin_link(self, browser: WebDriver):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page(self, browser: WebDriver):
        page = MainPage(browser, link)                          # Page Object init
        page.open()                                             # Open page in browser
        page.go_to_login_page()                                 # Execute go_to_login_page method
        login_page = LoginPage(browser, browser.current_url)    # Init Login Page object
        login_page.should_be_login_page()                       # Assertion if current page is login page


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: WebDriver):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_text()
