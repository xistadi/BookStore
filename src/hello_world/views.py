from django.views.generic import ListView
from products.models import Book
from django.shortcuts import render


class ShowBookListView(ListView):
    queryset = Book.objects.order_by('-pk')
    template_name = 'hello_world/homepage.html'
    paginate_by = 8


def index(request):
    return render(request, 'hello_world/homepage.html', context={})
