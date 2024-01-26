from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase

from lists.views import home_page
from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual('A new list item', Item.objects.first().text)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_save_item_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    def test_save_and_retrieve_item(self):
        first_item = Item()
        first_item.text = 'The first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, 'The first item')

        second_saved_item = saved_items[1]
        self.assertEqual(second_saved_item.text, 'The second item')
