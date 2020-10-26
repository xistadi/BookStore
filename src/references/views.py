from django.shortcuts import render
from .models import Genre, Author, Series, Publisher


def show_references_view(request):
    """Return a list of References obj"""
    genres = Genre.objects.all()
    authors = Author.objects.all()
    seriess = Series.objects.all()
    publishers = Publisher.objects.all()
    context = {'genres': genres, 'authors': authors, 'seriess': seriess, 'publishers': publishers}
    return render(request, template_name='references/ref_list.html', context=context)


def show_reference_by_pk_view(request, title, ref_pk):
    """Return Reference by pk obj"""
    if title == 'genre':
        type = Genre.objects.get(pk=ref_pk)
    elif title == 'author':
        type = Author.objects.get(pk=ref_pk)
    elif title == 'series':
        type = Series.objects.get(pk=ref_pk)
    elif title == 'publisher':
        type = Publisher.objects.get(pk=ref_pk)
    context = {'type': type}
    return render(request, template_name='references/ref.html', context=context)
