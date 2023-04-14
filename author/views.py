from django.views.generic import ListView, DetailView
from .models import Author
from book.models import Book


class AuthorList(ListView):
    model = Author
    template_name = "author/list.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "author/detail.html"
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        b = kwargs['object'].books.all()
        s = set(i.series for i in b if i.series)
        if s is not None:
            context['series'] = [{
                'title': series.name,
                'id': series.id,
                'books_count': series.actual_books_count,
                'books_planned': series.planned_books_count,
                'is_finished': series.actual_books_count == series.planned_books_count,
                'books': series.books.all()
            }
            for series in s]
        books = [{
            'title': book.title,
            'id': book.id,
            'series': book.series
        } for book in kwargs['object'].books.all()]
        context['books'] = books
        context['count'] = kwargs['object'].books.all().count()

        return context
