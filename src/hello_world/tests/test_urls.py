from django.test import SimpleTestCase
from django.urls import resolve, reverse

from hello_world import views


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('index:home')
        self.assertEquals(resolve(url).func.view_class, views.ShowBookListView)

    def test_sales_url(self):
        url = reverse('index:sales')
        self.assertEquals(resolve(url).func.view_class, views.ShowSales)
