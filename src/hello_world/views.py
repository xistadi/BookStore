from django.views.generic import ListView
from products.models import Book
import requests


class ShowBookListView(ListView):
    queryset = Book.objects.order_by('-pk')
    template_name = 'hello_world/homepage.html'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        url = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
        source = requests.get(url)
        all_rate = source.json()
        all_rate = [rate for rate in all_rate]
        context = super().get_context_data(**kwargs)
        last_some_books_first = Book.objects.order_by('-pk')[:6]
        last_some_books_second = Book.objects.order_by('-pk')[6:12]
        most_rated_book_first = Book.objects.order_by('-avr_rating')[:6]
        most_rated_book_second = Book.objects.order_by('-avr_rating')[6:12]
        context['all_rate'] = all_rate
        context['last_some_books_first'] = last_some_books_first
        context['last_some_books_second'] = last_some_books_second
        context['most_rated_book_first'] = most_rated_book_first
        context['most_rated_book_second'] = most_rated_book_second
        return context
