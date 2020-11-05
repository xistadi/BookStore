from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book


class ShowBookListView(ListView):
    model = Book


class ShowBookByPkView(DetailView):
    model = Book
    template_name = 'products/book.html'


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = forms.CreateBookForm
    template_name = 'products/create_book.html'
    success_url = '/books'


class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = forms.UpdateBookForm
    template_name = 'products/update_book.html'
    success_url = '/books'


class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books'
    template_name = 'products/delete_book.html'
