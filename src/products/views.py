from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms as formimport
from .models import Book


def show_book_by_pk_view(request, book_pk):
    name = Book.objects.get(pk=book_pk).name
    price = Book.objects.get(pk=book_pk).price
    author = Book.objects.get(pk=book_pk).author
    series = Book.objects.get(pk=book_pk).series
    genre = Book.objects.get(pk=book_pk).genre
    year = Book.objects.get(pk=book_pk).year
    context = {'name': name, 'price': price, 'author': author, 'series': series, 'genre': genre, 'year': year}
    return render(request, template_name='products/book.html', context=context)


def create_book_view(request):
    if request.method == 'POST':
        form = formimport.CreateBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = formimport.CreateBookForm()
    return render(request, template_name='products/create_book.html', context={'form': form, 'header': 'book'})
