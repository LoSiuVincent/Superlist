import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_start_a_list_and_retrieve_it_later(self):
        # Edith has a few todo items, so she enter the url to the browser to launch the app
        self.browser.get('http://localhost:8000')

        # She notices To-Do in the title and the header of the page
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('To-Do', header_text.text)

        # She is invited to enter a todo item right away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # 1. buy peacock feathers
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is another text box inviting her to enter another item.
        # She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page refreshes, and both items are shown on the list
        table = self.browser.find_element(By.ID, 'id_list_table')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # She wonders if the page remembers her items. The she see the page generates a unique URL.

        # She visits the URL. Her items are still here

        # Satisified. She goes back to sleep
        self.browser.quit()

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
