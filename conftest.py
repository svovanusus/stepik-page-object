import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action="store", default="en", help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None

    print("\n\nstart browser for test...\n")
    if language != None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options = options)
    else:
        browser = webdriver.Chrome()

    yield browser
    print("\n\nquit browser...\n")
    browser.quit()
