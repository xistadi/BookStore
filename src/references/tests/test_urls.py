from django.test import SimpleTestCase
from django.urls import resolve, reverse

from references import views


class TestUrls(SimpleTestCase):

    def test_reference_list_url(self):
        url = reverse('references:reference_view')
        self.assertEquals(resolve(url).func.view_class, views.ShowReferencesView)

    def test_genre_list_url(self):
        url = reverse('references:genre_list')
        self.assertEquals(resolve(url).func.view_class, views.ShowGenreListView)

    def test_author_list_url(self):
        url = reverse('references:author_list')
        self.assertEquals(resolve(url).func.view_class, views.ShowAuthorListView)

    def test_series_list_url(self):
        url = reverse('references:series_list')
        self.assertEquals(resolve(url).func.view_class, views.ShowSeriesListView)

    def test_publisher_list_url(self):
        url = reverse('references:publisher_list')
        self.assertEquals(resolve(url).func.view_class, views.ShowPublisherListView)

    def test_genre_by_pk_url(self):
        url = reverse('references:genre_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ShowGenreByPkView)

    def test_author_by_pk_url(self):
        url = reverse('references:author_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ShowAuthorByPkView)

    def test_series_by_pk_url(self):
        url = reverse('references:series_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ShowSeriesByPkView)

    def test_publisher_by_pk_url(self):
        url = reverse('references:publisher_by_pk', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ShowPublisherByPkView)

    def test_genre_create_url(self):
        url = reverse('references:genre_create')
        self.assertEquals(resolve(url).func.view_class, views.CreateGenreView)

    def test_author_create_url(self):
        url = reverse('references:author_create')
        self.assertEquals(resolve(url).func.view_class, views.CreateAuthorView)

    def test_series_create_url(self):
        url = reverse('references:series_create')
        self.assertEquals(resolve(url).func.view_class, views.CreateSeriesView)

    def test_publisher_create_url(self):
        url = reverse('references:publisher_create')
        self.assertEquals(resolve(url).func.view_class, views.CreatePublisherView)

    def test_genre_update_url(self):
        url = reverse('references:genre_update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateGenreView)

    def test_author_update_url(self):
        url = reverse('references:author_update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateAuthorView)

    def test_series_update_url(self):
        url = reverse('references:series_update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateSeriesView)

    def test_publisher_update_url(self):
        url = reverse('references:publisher_update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdatePublisherView)

    def test_genre_delete_url(self):
        url = reverse('references:genre_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteGenreView)

    def test_author_delete_url(self):
        url = reverse('references:author_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteAuthorView)

    def test_series_delete_url(self):
        url = reverse('references:series_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteSeriesView)

    def test_publisher_delete_url(self):
        url = reverse('references:publisher_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeletePublisherView)
