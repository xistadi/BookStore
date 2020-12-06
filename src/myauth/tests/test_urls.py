from django.test import SimpleTestCase
from django.urls import resolve, reverse

from myauth import views


class TestUrls(SimpleTestCase):

    def test_profile_by_pk_url(self):
        url = reverse('profile_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ShowProfileByPkView)

    def test_list_profile_url(self):
        url = reverse('list_profile')
        self.assertEquals(resolve(url).func.view_class, views.ListProfileView)

    def test_update_profile_url(self):
        url = reverse('update_profile')
        self.assertEquals(resolve(url).func.view_class, views.ProfileUpdateView)

    def test_update_profile_by_pk_url(self):
        url = reverse('update_profile_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ProfileUpdateByPkView)

    def test_create_card_url(self):
        url = reverse('create_card')
        self.assertEquals(resolve(url).func.view_class, views.CreateCreditCartView)

    def test_delete_card_url(self):
        url = reverse('delete_card')
        self.assertEquals(resolve(url).func.view_class, views.DeleteCreditCartView)

    def test_create_address_url(self):
        url = reverse('create_address')
        self.assertEquals(resolve(url).func.view_class, views.CreateProfileAddressView)

    def test_delete_address_url(self):
        url = reverse('delete_address')
        self.assertEquals(resolve(url).func.view_class, views.DeleteProfileAddressView)

    def test_update_address_url(self):
        url = reverse('update_address', kwargs={'number': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateProfileAddressView)
