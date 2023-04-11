from django.views.generic import ListView, DetailView
from .models import Author


class AuthorList(ListView):
    model = Author
    template_name = "author/list.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "author/detail.html"
    context_object_name = 'author'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = [{
            'title': book.title,
            'id': book.id
        } for book in kwargs['object'].books.all()]
        context['books'] = books

        return context