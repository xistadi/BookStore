from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import View
from .models import CommentProducts
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin

from products.models import Book

from . import forms


class CreateCommentView(LoginRequiredMixin, View):
    """Создаем комментарий"""
    def post(self, request, *args, **kwargs):
        form = forms.CreateCommentForm(request.POST)
        book = Book.objects.get(pk=kwargs.get('pk'))
        profile = self.request.user.profile
        stars = self.request.POST.get('stars')
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.book = book
            form.stars = stars
            form.save()
            avr = book.get_rating()
            book.avr_rating = avr
            book.save()
        book_pk = kwargs.get('pk')
        return redirect(f'/books/{book_pk}')


class UpdateCommentView(UserPassesTestMixin, UpdateView):
    """Обновляем комментарий"""
    model = CommentProducts
    form_class = forms.CreateCommentForm
    template_name = 'comment/update_comment.html'
    permission_required = 'comment.change_commentproducts'

    def get_success_url(self):
        comment = CommentProducts.objects.get(pk=self.kwargs['pk'])
        book = comment.book
        avr = book.get_rating()
        book.avr_rating = avr
        book.save()
        book_pk = comment.book.pk
        return reverse_lazy('products:book_by_pk', kwargs={'pk': book_pk})

    def test_func(self):
        comment_pk = self.kwargs.get("pk")
        comment = CommentProducts.objects.filter(pk=comment_pk).first()
        return self.request.user.is_staff or self.request.user == comment.profile.user

    def handle_no_permission(self):
        return redirect('login')


class DeleteCommentView(UserPassesTestMixin, DeleteView):
    """Удаляем комментарий"""
    model = CommentProducts
    template_name = 'products/delete_book.html'
    permission_required = 'comment.delete_commentproducts'

    def get_success_url(self):
        comment = CommentProducts.objects.get(pk=self.kwargs['pk'])
        book_pk = comment.book.pk
        return reverse_lazy('products:book_by_pk', kwargs={'pk': book_pk})

    def test_func(self):
        comment_pk = self.request.POST.get('comment_pk')
        comment = CommentProducts.objects.filter(pk=comment_pk).first()
        return self.request.user.is_staff or self.request.user == comment.profile.user

    def handle_no_permission(self):
        return redirect('login')

