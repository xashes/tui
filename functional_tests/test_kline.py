from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_input_symbol_and_display_kline(self):
        # Keller has heard about a online market charts app. He goes to checkout
        # its homepage
        self.browser.get('http://localhost:8000/charts/kline')

        # He notices the page title and header mention "Kline"
        self.assertIn('Kline', self.browser.title)

        # He is invited to enter a symbol straight away.
        inputbox = self.browser.find_element_by_id('id_symbol')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a symbol'
        )

        # He types "000001.SH" into a text box
        sample_symbol = '000001.SH'
        inputbox.send_keys(sample_symbol)

        # When she hits enter, the page updates, and now the page display a kline
        # chart with the symbol displayed at the top.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.fail('Finish the test.')


if __name__ == '__main__':
    unittest.main()
