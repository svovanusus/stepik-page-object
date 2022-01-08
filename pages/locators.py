from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn:not(.dropdown-menu a.btn)")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, ".basket-mini-inc a.btn:not(.dropdown-menu a.btn)")


class MainPageLocators(BasePageLocators):
    pass


class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_MESSAGES = (By.CSS_SELECTOR, ".alert .alertinner")
    IMPORTANT_INFO_IN_ALERT = (By.CSS_SELECTOR, "strong")


class BasketPageLocators(BasePageLocators):
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket_summary .basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, ".page_inner .content #content_inner p")
