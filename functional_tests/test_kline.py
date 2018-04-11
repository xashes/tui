import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


MAX_WAIT = 3

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, table_id, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id(table_id)
                rows = self.browser.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_input_symbol_and_display_kline(self):
        # Helen has heard about a online market charts app. She goes to checkout
        # its charts page
        self.browser.get(f'{self.live_server_url}/charts/kline')

        # She notices the page title and header mention "Kline"
        self.assertIn('Kline', self.browser.title)

        # She is invited to enter a symbol straight away.
        inputbox = self.browser.find_element_by_id('id_symbol')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a symbol')

        # She types "000001.SH" into a text box
        sample_symbol = '000001.SH'
        sample_symbol2 = '000002.SH'
        inputbox.send_keys(sample_symbol)

        # When she hits enter, the page updates, and now the page display a kline
        # chart with the symbol displayed as the chart title.
        # There's also a table displays symbols that her recently viewed.
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('id_recent_table', sample_symbol)
        self.fail('Finish the test.')

        # There is still a text box for her to enter another symbol. She enters
        # '000002.SH'
        inputbox = self.browser.find_element_by_id('id_symbol')
        inputbox.send_keys(sample_symbol2)
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both symbols on the recently
        # viewed table with this symbol on the top, and display the kline
        # chart for this symbol.
        self.wait_for_row_in_list_table('id_recent_table', sample_symbol)
        self.wait_for_row_in_list_table('id_recent_table', sample_symbol2)
        self.fail('Finish the test for kline chart')
