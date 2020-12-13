from django.test import SimpleTestCase
from references import forms


class TestForms(SimpleTestCase):

    def test_create_genre_form_valid_data(self):
        """test create genre form with valid data"""
        form = forms.CreateGenreForm(data={
            'name': 'test',
            'description': 'test'
        })
        self.assertTrue(form.is_valid())

    def test_create_genre_form_no_data(self):
        """test create genre form with no data"""
        form = forms.CreateGenreForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_author_form_valid_data(self):
        """test create author form with valid data"""
        form = forms.CreateAuthorForm(data={
            'name': 'test',
            'description': 'test'
        })
        self.assertTrue(form.is_valid())

    def test_create_author_form_no_data(self):
        """test create author form with no data"""
        form = forms.CreateAuthorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_series_form_valid_data(self):
        """test create series form with valid data"""
        form = forms.CreateSeriesForm(data={
            'name': 'test',
            'description': 'test'
        })
        self.assertTrue(form.is_valid())

    def test_create_series_form_no_data(self):
        """test create series form with no data"""
        form = forms.CreateSeriesForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_publisher_form_valid_data(self):
        """test create publisher form with valid data"""
        form = forms.CreatePublisherForm(data={
            'name': 'test',
            'description': 'test'
        })
        self.assertTrue(form.is_valid())

    def test_create_publisher_form_no_data(self):
        """test create publisher form with no data"""
        form = forms.CreatePublisherForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
