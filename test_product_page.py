from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver
import pytest


@pytest.mark.parametrize("promo", ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                pytest.param("offer7", marks=pytest.mark.xfail),
                                "offer8", "offer9"])
@pytest.mark.skip
def test_quest_can_add_product_to_basket(browser: WebDriver, promo: str):
    page = ProductPage(browser, f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}")
    page.open()
    page.add_to_basket()
    page.should_be_add_to_basket_alert()
    page.should_be_basket_state_alert()


def test_guest_should_see_login_link_on_product_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_success_message()
