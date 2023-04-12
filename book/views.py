from django.views.generic import ListView, DetailView
from .models import Book, BookSeries


class BookList(ListView):
    model = Book
    template_name = "book/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = [{
            'id': book.id,
            'title': book.title,
            'authors': book.display_authors()
        } for book in Book.objects.all()]
        context['books'] = books
        return context


class BookDetail(DetailView):
    model = Book
    template_name = "book/detail.html"
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        from book.models import BookSeries
        context = super().get_context_data(**kwargs)
        authors = [{
            'id': author.id,
            'fullname': author.fullname
        } for author in kwargs['object'].authors.all()]
        series_queryset = kwargs['object'].series
        if series_queryset is not None:
            form = BookSeries.SeriesName(
                    value=series_queryset.form_name).name.lower()
            series = {
                'id': series_queryset.id,
                'title': f"{series_queryset.name} {form}",
                'book_number': kwargs['object'].order_in_series
            }
            context['series'] = series
        context['authors'] = authors
        return context


class BookSeriesList(ListView):
    model = BookSeries
    template_name = "book/series-list.html"


class BookSeriesDetail(DetailView):
    model = BookSeries
    template_name = "book/series-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        books = [{
            'id': book.id,
            'title': book.title
        } for book in kwargs['object'].books.all()]
        context['books'] = books

        print(context)
        return context

