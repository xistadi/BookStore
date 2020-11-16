from django.views.generic import ListView
from products.models import Book
import requests
import itertools



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
        context['all_rate'] = all_rate
        context['last_some_books_first'] = last_some_books_first
        context['last_some_books_second'] = last_some_books_second
        return context
