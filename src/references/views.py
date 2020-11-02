from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Genre, Author, Series, Publisher
from . import forms


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
    context = {'type': type, 'ref_pk': ref_pk}
    return render(request, template_name='references/ref.html', context=context)


def create_genre_view(request):
    """Create new Genre obj"""
    if request.method == 'POST':
        form = forms.CreateGenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = forms.CreateGenreForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'genre'})


def create_author_view(request):
    """Create new Author obj"""
    if request.method == 'POST':
        form = forms.CreateAuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = forms.CreateAuthorForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'author'})


def create_series_view(request):
    """Create new Series obj"""
    if request.method == 'POST':
        form = forms.CreateSeriesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = forms.CreateSeriesForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'series'})


def create_publisher_view(request):
    """Create new Publisher obj"""
    if request.method == 'POST':
        form = forms.CreatePublisherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = forms.CreatePublisherForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'publisher'})


def update_genre_view(request, pk):
    """Update Genre obj by pk"""
    if request.method == 'POST':
        form = forms.UpdateGenreForm(data=request.POST)
        if form.is_valid():
            old_ref = Genre.objects.get(pk=pk)
            new_ref = forms.UpdateGenreForm(request.POST, instance=old_ref)
            new_ref.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Genre.objects.get(pk=pk)
        form = forms.UpdateGenreForm(instance=ref)
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'genre'})


def update_author_view(request, pk):
    """Update Author obj by pk"""
    if request.method == 'POST':
        form = forms.UpdateAuthorForm(data=request.POST)
        if form.is_valid():
            old_ref = Author.objects.get(pk=pk)
            new_ref = forms.UpdateAuthorForm(request.POST, instance=old_ref)
            new_ref.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Author.objects.get(pk=pk)
        form = forms.UpdateAuthorForm(instance=ref)
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'author'})


def update_series_view(request, pk):
    """Update Series obj by pk"""
    if request.method == 'POST':
        form = forms.UpdateSeriesForm(data=request.POST)
        if form.is_valid():
            old_ref = Series.objects.get(pk=pk)
            new_ref = forms.UpdateSeriesForm(request.POST, instance=old_ref)
            new_ref.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Series.objects.get(pk=pk)
        form = forms.UpdateSeriesForm(instance=ref)
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'series'})


def update_publisher_view(request, pk):
    """Update Publisher obj by pk"""
    if request.method == 'POST':
        form = forms.UpdatePublisherForm(data=request.POST)
        if form.is_valid():
            old_ref = Publisher.objects.get(pk=pk)
            new_ref = forms.UpdatePublisherForm(request.POST, instance=old_ref)
            new_ref.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Publisher.objects.get(pk=pk)
        form = forms.UpdatePublisherForm(instance=ref)
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'publisher'})


def delete_genre_view(request, pk):
    """Delete Genre obj by pk"""
    if request.method == 'POST':
        obj = Genre.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'genre'}
    return render(request, template_name='references/delete_reference.html', context=context)


def delete_author_view(request, pk):
    """Delete Author obj by pk"""
    if request.method == 'POST':
        obj = Author.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'author'}
    return render(request, template_name='references/delete_reference.html', context=context)


def delete_series_view(request, pk):
    """Delete Series obj by pk"""
    if request.method == 'POST':
        obj = Series.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'series'}
    return render(request, template_name='references/delete_reference.html', context=context)


def delete_publisher_view(request, pk):
    """Delete Publisher obj by pk"""
    if request.method == 'POST':
        obj = Publisher.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'publisher'}
    return render(request, template_name='references/delete_reference.html', context=context)
