import math
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser: WebDriver, url: str, timeout:int=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how: By, what: str):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present(self, how: By, what: str, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, how: By, what: str, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link in not presented!"


    def go_to_login_page(self):
        link: WebElement = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    def go_to_basket_page(self):
        link: WebElement = None
        try:
            link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        except NoSuchElementException:
            assert False, "Basket link is not presented!"
        link.click()


    def solve_quize_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
