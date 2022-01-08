from selenium.webdriver.remote.webdriver import WebDriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_ligin_link(browser: WebDriver):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser: WebDriver):
    page = MainPage(browser, link)                          # Page Object init
    page.open()                                             # Open page in browser
    page.go_to_ligin_page()                                 # Execute go_to_login_page method
    login_page = LoginPage(browser, browser.current_url)    # Init Login Page object
    login_page.should_be_login_page()                       # Assertion if current page is login page
