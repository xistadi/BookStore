from django.test import SimpleTestCase, TestCase
from myauth import forms


class TestForms(TestCase):

    def test_sing_up_form_valid_data(self):
        """test sing up form with valid data"""
        form = forms.SignUpForm(data={
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@gmail.com',
            'password1': '1234567!',
            'password2': '1234567!'
        })
        self.assertTrue(form.is_valid())

    def test_sing_up_form_no_data(self):
        """test sing up form with no data"""
        form = forms.SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_user_update_form_valid_data(self):
        """test user update form with valid data"""
        form = forms.UserUpdateForm(data={
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@gmail.com',
        })
        self.assertTrue(form.is_valid())

    def test_user_update_form_no_data(self):
        """test user update form with no data"""
        form = forms.UserUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_profile_update_form_valid_data(self):
        """test profile update form with valid data"""
        form = forms.ProfileUpdateForm(data={
            'phone_number': 'test',
        })
        self.assertTrue(form.is_valid())

    def test_profile_update_form_no_data(self):
        """test profile update form with no data"""
        form = forms.ProfileUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_profile_update_address_form_valid_data(self):
        """test profile update address form with valid data"""
        form = forms.ProfileAddressUpdateForm(data={
            'country': 'test',
            'city': 'test',
            'index': 'test',
            'address1': 'test',
            'address2': 'test',
        })
        self.assertTrue(form.is_valid())

    def test_profile_update_address_form_no_data(self):
        """test profile update address form with no data"""
        form = forms.ProfileAddressUpdateForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_profile_update_card_form_valid_data(self):
        """test profile update card form with valid data"""
        form = forms.CreditCardUpdateForm(data={
            'number': 1,
            'data_cart': 'test',
            'name': 'test',
            'cvv': 1
        })
        self.assertTrue(form.is_valid())

    def test_profile_update_card_form_no_data(self):
        """test profile update card form with no data"""
        form = forms.CreditCardUpdateForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
