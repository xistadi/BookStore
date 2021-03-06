from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = [
            'phone_number',
            'image'
            ]


class ProfileAddressUpdateForm(forms.ModelForm):

    class Meta:
        model = models.ProfileAddress
        fields = [
            'country',
            'city',
            'index',
            'address1',
            'address2',
            ]


class CreditCardUpdateForm(forms.ModelForm):

    class Meta:
        model = models.CreditCart
        fields = [
            'number',
            'data_cart',
            'name',
            'cvv'
            ]
