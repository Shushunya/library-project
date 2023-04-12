# Generated by Django 4.2 on 2023-04-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_options_alter_bookseries_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='lit_form',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Poetry'), (2, 'Drama'), (3, 'Prose')], default=3),
        ),
    ]