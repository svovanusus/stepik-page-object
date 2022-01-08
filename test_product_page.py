from .pages.product_page import ProductPage
from selenium.webdriver.remote.webdriver import WebDriver
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_quest_can_add_product_to_basket(browser: WebDriver):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_add_to_basket_alert()
    page.should_be_basket_state_alert()
    #time.sleep(3600)
