from django.contrib import admin
from .models import Author


class BookInline(admin.TabularInline):
    model = Author.books.through


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ['fullname',]
    fields = [
        ('first_name', 'last_name'),
    ]
    inlines = [
        BookInline,
    ]
