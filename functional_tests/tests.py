import unittest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 5 


class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                elapsed_time = time.time() - start_time
                if elapsed_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Edith has a few todo items, so she enter the url to the browser to launch the app
        self.browser.get(self.live_server_url)

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

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is another text box inviting her to enter another item.
        # She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page refreshes, and both items are shown on the list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Satisified. She goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices her list has a unqiue URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.

        ## We use a new broswer session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis vists the home page. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)

        # Francis starts a new item by entering a new item.
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milks')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Buy milks')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(edith_list_url, francis_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathres', page_text)
        self.assertIn('Buy milks', page_text)
