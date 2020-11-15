from django.views.generic import ListView
from products.models import Book
import requests
import itertools
from django.shortcuts import render


class ShowBookListView(ListView):
    queryset = Book.objects.order_by('-pk')
    template_name = 'hello_world/homepage.html'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        url = 'https://v6.exchangerate-api.com/v6/6017e270509ccbc1766d3ba6/latest/USD'
        source = requests.get(url)
        exchange_rate = source.json()
        all_rate = exchange_rate['conversion_rates']
        all_rate = dict(itertools.islice(all_rate.items(), 20))
        base_rate = exchange_rate['base_code']
        context = super().get_context_data(**kwargs)
        last_some_books_first = Book.objects.order_by('-pk')[:6]
        last_some_books_second = Book.objects.order_by('-pk')[6:12]
        context['all_rate'] = all_rate
        context['base_rate'] = base_rate
        context['last_some_books_first'] = last_some_books_first
        context['last_some_books_second'] = last_some_books_second
        return context
