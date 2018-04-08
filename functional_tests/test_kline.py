import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_input_symbol_and_display_kline(self):
        # Helen has heard about a online market charts app. She goes to checkout
        # its homepage
        self.browser.get('http://localhost:8000/charts/kline')

        # She notices the page title and header mention "Kline"
        self.assertIn('Kline', self.browser.title)

        # She is invited to enter a symbol straight away.
        inputbox = self.browser.find_element_by_id('id_symbol')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a symbol')

        # She types "000001.SH" into a text box
        sample_symbol = '000001.SH'
        inputbox.send_keys(sample_symbol)

        # When she hits enter, the page updates, and now the page display a kline
        # chart with the symbol displayed at the top.
        inputbox.send_keys(Keys.ENTER)
