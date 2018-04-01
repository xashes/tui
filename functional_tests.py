import pytest


# Keller has heard about a online market charts app. He goes to checkout
# its homepage
@pytest.fixture(scope='module')
def browser():
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')
    return browser

def test_can_input_symbol_and_display_charts(browser):
    # He notices the page title and header mention "charts"
    assert 'Charts' in browser.title
    pytest.fail('Finish the test.')
