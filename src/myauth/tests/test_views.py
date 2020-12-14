from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from myauth import models


User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        """setUp for order test views"""
        group = Group.objects.get(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        self.user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        self.profile = self.user.profile
        models.ProfileAddress.objects.create(profile=self.profile, country='unit_test', city='unit_test',
                                                    index='unit_test', address1='unit_test', address2='unit_test')
        self.session = self.client.session
        self.my_account_url = reverse('myaccount')
        self.list_profile_url = reverse('list_profile')
        self.update_profile_url = reverse('update_profile')
        self.create_card_url = reverse('create_card')
        self.delete_card_url = reverse('delete_card')
        self.create_address_url = reverse('create_address')
        self.delete_address_url = reverse('delete_address')

    def test_my_account_view(self):
        """test show my account view"""
        response = self.client.get(self.my_account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_account.html')

    def test_profile_by_pk_view(self):
        """test show profile by pk view"""
        user = User.objects.create_user('unittest1', password='unittest')
        response = self.client.get('/accounts/1/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myauth/profile_by_pk.html')

    def test_list_profile_view(self):
        """test show list profile view"""
        response = self.client.get(self.list_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myauth/profile_list.html')

    def test_update_profile_view(self):
        """test update profile view"""
        response = self.client.post(self.update_profile_url, {
            'username': 'unittest',
            'first_name': 'unittest',
            'last_name': 'unittest',
            'email': 'unittest@gmail.com',
            'phone_number': '2323',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().phone_number, '2323')

    def test_update_profile_by_pk_view(self):
        """test update profile by pk view"""
        response = self.client.post('/accounts/update_by_pk/1/', {
            'username': 'unittest',
            'first_name': 'unittest',
            'last_name': 'unittest',
            'email': 'unittest@gmail.com',
            'phone_number': '23231',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().phone_number, '23231')

    def test_create_card_view(self):
        """test create card view"""
        response = self.client.post(self.create_card_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().credit_cards.count(), 1)

    def test_delete_card_view(self):
        """test delete card view"""
        models.CreditCart.objects.create(profile=self.profile, number=232, data_cart='2323', name='test', cvv=23)
        response = self.client.post(self.delete_card_url, {'pk': 1})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().credit_cards.count(), 0)

    def test_create_address_view(self):
        """test create address view"""
        response = self.client.post(self.create_address_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().profile_address.count(), 2)

    def test_delete_address_view(self):
        """test delete address view"""
        response = self.client.post(self.delete_address_url, {'pk': 1})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().profile_address.count(), 0)

    def test_update_address_view(self):
        """test update address view"""
        response = self.client.post('/accounts/update_address/1/', {
            'country': 'test_update',
            'city': 'test_update',
            'index': 'test_update',
            'address1': 'test_update',
            'address2': 'test_update',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Profile.objects.last().profile_address.last().country, 'test_update')
