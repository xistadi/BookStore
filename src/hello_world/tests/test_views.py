from django.test import TestCase, Client
from django.urls import reverse

from hello_world import views


class TestViews(TestCase):

    def setUp(self):
        """setUp for hello_world test view"""
        self.client = Client()
        self.home_url = reverse('index:home')
        self.sales_url = reverse('index:sales')

    def test_show_homepage_view(self):
        """test show homepage"""
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello_world/homepage.html')

    def test_show_sales_view(self):
        """test show sales"""
        response = self.client.get(self.sales_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello_world/sales.html')
