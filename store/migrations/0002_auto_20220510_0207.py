# Generated by Django 3.1 on 2022-05-09 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Images',
            new_name='images',
        ),
    ]
