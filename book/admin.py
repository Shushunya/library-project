from django.contrib import admin
from .models import Book, BookSeries


@admin.register(BookSeries)
class BookSeriesAdmin(admin.ModelAdmin):
    model = BookSeries
    list_display = ['name', 'actual_books_count', 'form_name', 'planned_books_count']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'display_authors', 'series',
                    'order_in_series', ]
    fields = [
        'title',
        'series',
        'order_in_series',
        'lit_form',
    ]

