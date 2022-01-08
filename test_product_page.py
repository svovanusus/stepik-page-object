from .pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver
import pytest


#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_template = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={}"


@pytest.mark.parametrize("promo", ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                pytest.param("offer7", marks=pytest.mark.xfail),
                                "offer8", "offer9"])
@pytest.mark.skip
def test_quest_can_add_product_to_basket(browser: WebDriver, promo: str):
    page = ProductPage(browser, link_template.format(promo))
    page.open()
    page.add_to_basket()
    page.should_be_add_to_basket_alert()
    page.should_be_basket_state_alert()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser: WebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_success_message()
