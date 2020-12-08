from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session

from coupon import models
from cart.views import create_cart

User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
        group = Group.objects.create(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        user.is_superuser = True
        user.is_staff = True
        user.save()
        self.list_coupon_url = reverse('coupon:list_coupon')

    def test_list_coupon_view(self):
        """test book list"""
        response = self.client.get(self.list_coupon_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'coupon/coupon_list.html')
