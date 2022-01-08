from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button: WebElement = None

        try:
            button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        except NoSuchElementException:
            assert False, "Add to basket buttn is not presented!"

        if button == None:
            assert False, "Unknown error"

        button.click()
        self.solve_quize_and_get_code()


    def should_be_add_to_basket_alert(self):
        product_name_el: WebElement = None
        try:
            product_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        except NoSuchElementException:
            assert False, "Product name is not presented!"

        if product_name_el == None:
            assert False, "Unknown error"

        product_name: str = product_name_el.text

        found_product_alert = False
        alerts: list[WebElement] = self.browser.find_elements(*ProductPageLocators.ALLERT_MESSAGES)
        for alert in alerts:
            if "has been added" in alert.text:
                found_product_alert = True
                try:
                    important_info_el: WebElement = alert.find_element(*ProductPageLocators.IMPORTANT_INFO_IN_ALERT)
                    assert important_info_el.text == product_name, "Product name in alert is not correct!"
                except NoSuchElementException:
                    assert False, "Product name is not presented in Product added alert!"
        assert found_product_alert, "Product added alert wasn't been found!"


    def should_be_basket_state_alert(self):
        product_price_el: WebElement = None
        try:
            product_price_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        except NoSuchElementException:
            assert False, "Product price is not presented!"

        if product_price_el == None:
            assert False, "Unknown error"

        product_price: str = product_price_el.text

        found_basket_info_alert = False
        alerts: list[WebElement] = self.browser.find_elements(*ProductPageLocators.ALLERT_MESSAGES)
        for alert in alerts:
            if "basket total" in alert.text:
                found_basket_info_alert = True
                try:
                    important_info_el: WebElement = alert.find_element(*ProductPageLocators.IMPORTANT_INFO_IN_ALERT)
                    assert important_info_el.text == product_price, f"Basket total value ({important_info_el.text}) is not equal product price ({product_price})!"
                except NoSuchElementException:
                    assert False, "Basket total value is not presented in Basket total alert!"
        assert found_basket_info_alert, "Basket total alert is not found!"
