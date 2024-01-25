import unittest
from selenium import webdriver

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
    
    def test_start_a_list_and_retrieve_it_later(self):
        # Edith has a few todo items, so she enter the url to the browser to launch the app
        self.browser.get('http://localhost:8000')

        # She notices To-Do in the title of the page
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a todo item right away

        # She types "buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # 1. buy peacock feathers

        # There is another text box inviting her to enter another item.
        # She enters "Use peacock feathers to make a fly"

        # The page refreshes, and both items are shown on the list

        # She wonders if the page remembers her items. The she see the page generates a unique URL.

        # She visits the URL. Her items are still here

        # Satisified. She goes back to sleep
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()