# Generated by Django 4.2 on 2023-04-11 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'default_related_name': 'books', 'ordering': ['series', 'order_in_series', 'title']},
        ),
        migrations.AlterModelOptions(
            name='bookseries',
            options={'default_related_name': 'book_series', 'verbose_name_plural': 'book series'},
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='author.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='book.bookseries'),
        ),
    ]
