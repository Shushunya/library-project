# Generated by Django 4.2 on 2023-04-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_lit_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookseries',
            name='form_name',
            field=models.PositiveSmallIntegerField(choices=[('1', 'Standalone'), ('2', 'Duology'), ('3', 'Trilogy'), ('4', 'Quartet')], default='1'),
        ),
    ]
