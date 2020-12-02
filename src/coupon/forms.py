from django import forms

from . import models


class CreateCouponForm(forms.ModelForm):
    class Meta:
        model = models.Coupon
        fields = ('__all__')
