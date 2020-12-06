from django.test import SimpleTestCase
from django.urls import resolve, reverse

from comment import views


class TestUrls(SimpleTestCase):

    def test_create_comment_url(self):
        url = reverse('comment:create_comment', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.CreateCommentView)

    def test_delete_comment_url(self):
        url = reverse('comment:delete_comment', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteCommentView)

    def test_update_comment_url(self):
        url = reverse('comment:update_comment', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateCommentView)
