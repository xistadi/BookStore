from django.test import SimpleTestCase
from django.urls import resolve, reverse

from products import views


class TestUrls(SimpleTestCase):

    def test_book_list_url(self):
        url = reverse('products:book_list')
        self.assertEquals(resolve(url).func.view_class, views.ShowBookListView)

    def test_book_by_pk_url(self):
        url = reverse('products:book_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ShowBookByPkView)

    def test_create_new_book_url(self):
        url = reverse('products:create_new_book')
        self.assertEquals(resolve(url).func.view_class, views.CreateBookView)

    def test_update_book_by_pk_url(self):
        url = reverse('products:update_book_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateBookView)

    def test_delete_book_by_pk_url(self):
        url = reverse('products:delete_book_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteBookView)

    def test_search_results_url(self):
        url = reverse('products:search_results')
        self.assertEquals(resolve(url).func.view_class, views.SearchBookView)
