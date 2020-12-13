from django import forms
from . import models


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = [
            'comment',
            ]


class OrderDeliveryStatusUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = [
            'delivery_status'
        ]


class OrderUpdateForManagersForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = [
            'delivery_status',
            'comment'
        ]
