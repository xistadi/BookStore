from django import forms

from . import models


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentProducts
        fields = ('comment',)
