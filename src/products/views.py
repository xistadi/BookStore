from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import Book


def show_books_view(request):
    """Return a list of Books obj"""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template_name='products/book_list.html', context=context)


def show_book_by_pk_view(request, book_pk):
    """Return Book obj by pk"""
    name = Book.objects.get(pk=book_pk).name
    price = Book.objects.get(pk=book_pk).price
    author = Book.objects.get(pk=book_pk).author
    series = Book.objects.get(pk=book_pk).series
    genre = Book.objects.get(pk=book_pk).genre
    year = Book.objects.get(pk=book_pk).year
    context = {'name': name, 'price': price, 'author': author, 'series': series, 'genre': genre, 'year': year}
    return render(request, template_name='products/book.html', context=context)


def create_book_view(request):
    """Create new Book obj"""
    if request.method == 'POST':
        form = forms.CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books')
    else:
        form = forms.CreateBookForm()
    return render(request, template_name='products/create_book.html', context={'form': form, 'header': 'book'})


def update_book_view(request, pk):
    """Update Book obj by pk"""
    if request.method == 'POST':
        form = forms.UpdateBookForm(request.POST, request.FILES)
        if form.is_valid():
            old_book = Book.objects.get(pk=pk)
            new_book = forms.UpdateBookForm(request.POST, request.FILES, instance=old_book)
            new_book.save()
            return HttpResponseRedirect('/books')
    else:
        book = Book.objects.get(pk=pk)
        form = forms.UpdateBookForm(instance=book)
    return render(request, template_name='products/update_book.html', context={'form': form, 'header': 'book'})


def delete_book_view(request, pk):
    """Delete Book obj by pk"""
    if request.method == 'POST':
        obj = Book.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/books')
    else:
        context = {'header': 'book'}
    return render(request, template_name='products/delete_book.html', context=context)
