# Generated by Django 4.2.4 on 2023-09-06 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_list',
            new_name='Books',
        ),
    ]
