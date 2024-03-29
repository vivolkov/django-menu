# Generated by Django 2.1.5 on 2019-01-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_menu', '0002_menu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='text',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
