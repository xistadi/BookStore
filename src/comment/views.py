from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import View
from .models import CommentProducts
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from products.models import Book

from . import forms


class CreateCommentView(View):
    def post(self, request, *args, **kwargs):
        form = forms.CreateCommentForm(request.POST)
        book = Book.objects.get(pk=kwargs.get('pk'))
        profile = self.request.user.profile
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.book = book
            form.save()
            print(self.request.POST.get('comment'))
            print(kwargs.get('pk'))
        book_pk = kwargs.get('pk')
        return redirect(f'/books/{book_pk}')


class UpdateCommentView(UpdateView):
    model = CommentProducts
    form_class = forms.CreateCommentForm
    template_name = 'comment/update_comment.html'

    def get_success_url(self):
        comment = CommentProducts.objects.get(pk=self.kwargs['pk'])
        book_pk = comment.book.pk
        return reverse_lazy('products:book_by_pk', kwargs={'pk': book_pk})


class DeleteCommentView(DeleteView):
    model = CommentProducts
    template_name = 'products/delete_book.html'

    def get_success_url(self):
        comment = CommentProducts.objects.get(pk=self.kwargs['pk'])
        book_pk = comment.book.pk
        return reverse_lazy('products:book_by_pk', kwargs={'pk': book_pk})
