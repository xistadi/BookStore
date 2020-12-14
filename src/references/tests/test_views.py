from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from references import models

User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        """setUp for references test views"""
        group = Group.objects.get(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        user.is_superuser = True
        user.is_staff = True
        user.save()
        self.reference_url = reverse('references:reference_view')
        self.genre_list_url = reverse('references:genre_list')
        self.author_list_url = reverse('references:author_list')
        self.series_list_url = reverse('references:series_list')
        self.publisher_list_url = reverse('references:publisher_list')
        self.genre_by_pk_url = reverse('references:genre_by_pk', kwargs={'pk': 1})
        self.author_by_pk_url = reverse('references:author_by_pk', kwargs={'pk': 1})
        self.series_by_pk_url = reverse('references:series_by_pk', kwargs={'pk': 1})
        self.publisher_by_pk_url = reverse('references:publisher_by_pk', kwargs={'pk': 1})
        self.genre_create_url = reverse('references:genre_create')
        self.author_create_url = reverse('references:author_create')
        self.series_create_url = reverse('references:series_create')
        self.publisher_create_url = reverse('references:publisher_create')
        self.genre_delete_url = reverse('references:genre_delete', kwargs={'pk': 1})
        self.author_delete_url = reverse('references:author_delete', kwargs={'pk': 1})
        self.series_delete_url = reverse('references:series_delete', kwargs={'pk': 1})
        self.publisher_delete_url = reverse('references:publisher_delete', kwargs={'pk': 1})
        self.test_genre = models.Genre.objects.create(name='test')
        self.test_author = models.Author.objects.create(name='test')
        self.test_series = models.Series.objects.create(name='test')
        self.test_publisher = models.Publisher.objects.create(name='test')

    def test_references_list_view(self):
        """test references list"""
        response = self.client.get(self.reference_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/all_references_list.html')

    def test_genre_list_view(self):
        """test genre list"""
        response = self.client.get(self.genre_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_list.html')

    def test_author_list_view(self):
        """test author list"""
        response = self.client.get(self.author_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_list.html')

    def test_series_list_view(self):
        """test series list"""
        response = self.client.get(self.series_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_list.html')

    def test_publisher_list_view(self):
        """test publisher list"""
        response = self.client.get(self.publisher_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_list.html')

    def test_genre_by_pk_view(self):
        """test genre by pk"""
        response = self.client.get(self.genre_by_pk_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_by_pk.html')

    def test_author_by_pk_view(self):
        """test author by pk"""
        response = self.client.get(self.author_by_pk_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_by_pk.html')

    def test_series_by_pk_view(self):
        """test series by pk"""
        response = self.client.get(self.series_by_pk_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_by_pk.html')

    def test_publisher_by_pk_view(self):
        """test publisher by pk"""
        response = self.client.get(self.publisher_by_pk_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'references/ref_by_pk.html')

    def test_genre_create_view(self):
        """test genre create"""
        response = self.client.post(self.genre_create_url, {
            'name': 'test1',
            'description': ''
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Genre.objects.last().name, 'test1')

    def test_author_create_view(self):
        """test author create"""
        response = self.client.post(self.author_create_url, {
            'name': 'test1',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Author.objects.last().name, 'test1')

    def test_series_create_view(self):
        """test series create"""
        response = self.client.post(self.series_create_url, {
            'name': 'test1',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Series.objects.last().name, 'test1')

    def test_publisher_create_view(self):
        """test publisher create"""
        response = self.client.post(self.publisher_create_url, {
            'name': 'test1'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Publisher.objects.last().name, 'test1')

    def test_genre_update_view(self):
        """test genre update"""
        response = self.client.post(f'/references/genre/update/{models.Genre.objects.last().pk}', {
            'name': 'testunittes'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Genre.objects.last().name, 'testunittes')

    def test_author_update_view(self):
        """test authore update"""
        response = self.client.post(f'/references/author/update/{models.Author.objects.last().pk}', {
            'name': 'testunittes'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Author.objects.last().name, 'testunittes')

    def test_series_update_view(self):
        """test series update"""
        response = self.client.post(f'/references/series/update/{models.Series.objects.last().pk}', {
            'name': 'testunittes'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Series.objects.last().name, 'testunittes')

    def test_publisher_update_view(self):
        """test publisher update"""
        response = self.client.post(f'/references/publisher/update/{models.Publisher.objects.last().pk}', {
            'name': 'testunittes'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Publisher.objects.last().name, 'testunittes')

    def test_genre_delete_view(self):
        """test genre delete"""
        response = self.client.post(self.genre_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Genre.objects.all().count(), 0)

    def test_author_delete_view(self):
        """test author delete"""
        response = self.client.post(self.author_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Author.objects.all().count(), 0)

    def test_series_delete_view(self):
        """test series delete"""
        response = self.client.post(self.series_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Series.objects.all().count(), 0)

    def test_publisher_delete_view(self):
        """test publisher delete"""
        response = self.client.post(self.publisher_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Publisher.objects.all().count(), 0)
