from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from django.db.models import Q


class ShowBookListView(ListView):
    model = Book
    paginate_by = 10


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


class SearchBookView(ListView):
    model = Book
    template_name = 'products/book_search_list.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('search')
        books = Book.objects.filter(Q(name__icontains=query))
        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('search')
        return context
