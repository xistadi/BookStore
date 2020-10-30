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


def update_book_view(request, pk):
    if request.method == 'POST':
        form = formimport.UpdateBookForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('name')
            ref_author = form.cleaned_data.get('author')
            obj = Book.objects.get(pk=pk)
            obj.name = ref_name
            obj.description = ref_author
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Book.objects.get(pk=pk)
        form = formimport.UpdateBookForm(data={'name': ref.name, 'author': ref.author})
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'book'})


def delete_book_view(request, pk):
    if request.method == 'POST':
        obj = Book.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'book'}
    return render(request, template_name='references/delete_reference.html', context=context)
