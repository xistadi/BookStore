from django.test import SimpleTestCase
from comment import forms


class TestForms(SimpleTestCase):

    def test_create_comment_form_valid_data(self):
        """test comment genre form with valid data"""
        form = forms.CreateCommentForm(data={
            'comment': 'test',
            'stars': 3
        })
        self.assertTrue(form.is_valid())

    def test_create_comment_form_no_data(self):
        """test create comment form with no data"""
        form = forms.CreateCommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
