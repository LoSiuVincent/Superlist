from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase

from lists.views import home_page
from lists.models import Item, List


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

        self.assertEqual(Item.objects.count(), 0)

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual('A new list item', Item.objects.first().text)

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


class ListViewTest(TestCase):
    def test_used_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_list_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')


class ListAndItemModelTest(TestCase):
    def test_save_and_retrieve_item(self):
        list_ = List()
        list_.save()
        
        first_item = Item()
        first_item.text = 'The first item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, 'The first item')
        self.assertEqual(first_saved_item.list, list_)

        second_saved_item = saved_items[1]
        self.assertEqual(second_saved_item.text, 'The second item')
        self.assertEqual(second_saved_item.list, list_)
