from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket items are not presented!"


    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket items are presented but should not!"


    def should_be_empty_basket_text(self):
        basket_empty_text: WebElement = None
        try:
            basket_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        except NoSuchElementException:
            assert False, "Basket empty text is not presented!"
        assert basket_empty_text.text != "", "Basket empty text is not presented!"
