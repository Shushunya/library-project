from django.views.generic import ListView, DetailView
from .models import Book


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
        context = super().get_context_data(**kwargs)
        authors = [{
            'id': author.id,
            'fullname': author.fullname
        } for author in kwargs['object'].authors.all()]
        context['authors'] = authors

        return context
