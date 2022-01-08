from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # Page Object init
    page.open()                     # Open page in browser
    page.go_to_ligin_page()         # Execute go_to_login_page method
