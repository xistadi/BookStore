from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from products.models import Book
from comment import models
from references import models as references_models

User = get_user_model()


class TestModels(TestCase):

    def setUp(self):
        """setUp for products test models"""
        group = Group.objects.create(name='Customers')
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

    def test_get_rating_no_comment_models(self):
        """test get rating with no comment"""
        rating = self.book.get_rating()
        self.assertEqual(rating, 0)

    def test_get_rating_with_comment_models(self):
        """test get rating with one comment"""
        comment = models.CommentProducts.objects.create(profile=self.user.profile, book=self.book,
                                                             comment='comment', stars=5)
        rating = self.book.get_rating()
        self.assertEqual(rating, 5)

    def test_get_rating_with_comments_models(self):
        """test get rating with two comments"""
        comment1 = models.CommentProducts.objects.create(profile=self.user.profile, book=self.book,
                                                             comment='comment', stars=5)
        comment2 = models.CommentProducts.objects.create(profile=self.user.profile, book=self.book,
                                                        comment='comment', stars=1)
        rating = self.book.get_rating()
        self.assertEqual(rating, 3)
