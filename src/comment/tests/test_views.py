from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from products.models import Book
from comment import models
from references import models as references_models

User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        """setUp for comment test views"""
        group = Group.objects.get(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        self.user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        self.author = references_models.Author.objects.create(name='unittest')
        self.series = references_models.Series.objects.create(name='unittest')
        self.genre = references_models.Genre.objects.create(name='unittest')
        self.publisher = references_models.Publisher.objects.create(name='unittest')
        self.book = Book.objects.create(name='unittest', price=1, series=self.series, binding=1, book_format='',
                                          isbn='', age_limit='', publisher=self.publisher, active=True)
        self.book.genre.set([1])
        self.book.author.set([1])
        self.comment = models.CommentProducts.objects.create(profile=self.user.profile, book=self.book,
                                                             comment='comment', stars=5)
        self.comment_create_url = reverse('comment:create_comment', kwargs={'pk': 1})
        self.comment_delete_url = reverse('comment:delete_comment', kwargs={'pk': 1})

    def test_create_comment_view(self):
        """test create comment"""
        response = self.client.post(self.comment_create_url, {
            'profile': self.user.profile,
            'book': self.book,
            'comment': 'unittest',
            'stars': 1
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.CommentProducts.objects.last().comment, 'unittest')

    def test_update_comment_view(self):
        """test update comment"""
        response = self.client.post(f'/comment/update/{models.CommentProducts.objects.last().pk}/', {
            'profile': self.user.profile,
            'book': self.book,
            'comment': 'testupdate',
            'stars': 1
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.CommentProducts.objects.last().comment, 'testupdate')

    def test_delete_comment_view(self):
        """test delete comment"""
        response = self.client.post(self.comment_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.CommentProducts.objects.all().count(), 0)
