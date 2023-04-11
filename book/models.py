from django.db import models
from author.models import Author


class BookSeries(models.Model):
    name = models.CharField(max_length=200)

    objects = models.Manager()

    @property
    def books_count(self):
        return self.books.all().count()

    class Meta:
        default_related_name = "book_series"
        verbose_name_plural = "book series"

    def __str__(self):
        return self.name

    def display_books(self):
        return ', '.join(book.title for book in self.books.all())


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    series = models.ForeignKey(BookSeries, on_delete=models.DO_NOTHING, null=True, blank=True)
    order_in_series = models.IntegerField(default=1)
    objects = models.Manager()

    class Meta:
        default_related_name = "books"
        ordering = ['series', 'order_in_series', 'title']
    def __str__(self):
        return self.title

    def display_authors(self):
        return ', '.join(a.fullname for a in self.authors.all()[:3])

    display_authors.short_description = "authors"

# add book instances (physical books in a library)
