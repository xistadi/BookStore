from django.test import SimpleTestCase
from django.urls import resolve, reverse

from cart import views


class TestUrls(SimpleTestCase):

    def test_cart_index_url(self):
        url = reverse('cart:cart_index')
        self.assertEquals(resolve(url).func.view_class, views.CartView)

    def test_delete_book_in_cart_url(self):
        url = reverse('cart:delete_book_in_cart', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteBookInCartView)

    def test_update_cart_url(self):
        url = reverse('cart:update_cart')
        self.assertEquals(resolve(url).func.view_class, views.UpdateCartView)
