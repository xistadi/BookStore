from django.test import SimpleTestCase
from django.urls import resolve, reverse

from order import views


class TestUrls(SimpleTestCase):

    def test_update_order_url(self):
        url = reverse('order:update_order')
        self.assertEquals(resolve(url).func.view_class, views.OrderUpdateView)

    def test_update_order_manager_url(self):
        url = reverse('order:update_order_manager', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateOrderForManagerByPkView)

    def test_update_order_status_url(self):
        url = reverse('order:update_order_status', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateStatusOrderView)

    def test_update_order_status_manager_url(self):
        url = reverse('order:update_order_status_manager', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateStatusOrderForManagerView)

    def test_cancel_order_url(self):
        url = reverse('order:cancel_order', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.CancelOrderView)

    def test_order_list_url(self):
        url = reverse('order:order_list')
        self.assertEquals(resolve(url).func.view_class, views.ListOrderView)
