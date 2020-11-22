from django import forms
from . import models


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = [
            'comment',
            ]
