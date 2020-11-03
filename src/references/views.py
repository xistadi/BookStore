from .models import Genre, Author, Series, Publisher
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from . import forms


class ShowReferencesView(TemplateView):
    template_name = 'references/all_references_list.html'

    def get_context_data(self, **kwargs):
        genres = Genre.objects.all()
        authors = Author.objects.all()
        seriess = Series.objects.all()
        publishers = Publisher.objects.all()
        context = super().get_context_data(**kwargs)
        context['genres'] = genres
        context['authors'] = authors
        context['seriess'] = seriess
        context['publishers'] = publishers
        return context


class ShowGenreListView(ListView):
    model = Genre
    template_name = 'references/ref_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Жанры книг'
        return context


class ShowAuthorListView(ListView):
    model = Author
    template_name = 'references/ref_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Авторы книг'
        return context


class ShowSeriesListView(ListView):
    model = Series
    template_name = 'references/ref_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Серии книг'
        return context


class ShowPublisherListView(ListView):
    model = Publisher
    template_name = 'references/ref_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Издательства книг'
        return context


class ShowGenreByPkView(DetailView):
    model = Genre
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'genre'
        return context


class ShowAuthorByPkView(DetailView):
    model = Author
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'author'
        return context


class ShowSeriesByPkView(DetailView):
    model = Series
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'series'
        return context


class ShowPublisherByPkView(DetailView):
    model = Publisher
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'publisher'
        return context


class CreateGenreView(CreateView):
    model = Genre
    form_class = forms.CreateGenreForm
    template_name = 'references/create_reference.html'
    success_url = '/references/genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'жанр'
        return context


class CreateAuthorView(CreateView):
    model = Author
    form_class = forms.CreateAuthorForm
    template_name = 'references/create_reference.html'
    success_url = '/references/author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'автора'
        return context


class CreateSeriesView(CreateView):
    model = Series
    form_class = forms.CreateSeriesForm
    template_name = 'references/create_reference.html'
    success_url = '/references/series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'серию'
        return context


class CreatePublisherView(CreateView):
    model = Publisher
    form_class = forms.CreatePublisherForm
    template_name = 'references/create_reference.html'
    success_url = '/references/publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'издательство'
        return context


class UpdateGenreView(UpdateView):
    model = Genre
    form_class = forms.UpdateGenreForm
    success_url = '/references/genre'
    template_name = 'references/update_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'жанр'
        return context


class UpdateAuthorView(UpdateView):
    model = Author
    form_class = forms.UpdateAuthorForm
    success_url = '/references/author'
    template_name = 'references/update_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'автора'
        return context


class UpdateSeriesView(UpdateView):
    model = Series
    form_class = forms.UpdateSeriesForm
    success_url = '/references/series'
    template_name = 'references/update_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'серию'
        return context


class UpdatePublisherView(UpdateView):
    model = Publisher
    form_class = forms.UpdatePublisherForm
    success_url = '/references/publisher'
    template_name = 'references/update_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'издательство'
        return context


class DeleteGenreView(DeleteView):
    model = Genre
    success_url = '/references/genre'
    template_name = 'references/delete_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'жанр'
        return context


class DeleteAuthorView(DeleteView):
    model = Author
    success_url = '/references/author'
    template_name = 'references/delete_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'автора'
        return context


class DeleteSeriesView(DeleteView):
    model = Series
    success_url = '/references/series'
    template_name = 'references/delete_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'серию'
        return context


class DeletePublisherView(DeleteView):
    model = Publisher
    success_url = '/references/publisher'
    template_name = 'references/delete_reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'издательство'
        return context
