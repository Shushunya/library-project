from django.db import models
from author.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name="books")

    objects = models.Manager()

    def __str__(self):
        return self.title

    def display_authors(self):
        return ', '.join(a.fullname for a in self.authors.all()[:3])

    display_authors.short_description = "authors"
