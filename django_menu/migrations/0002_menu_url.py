# Generated by Django 2.1.5 on 2019-01-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.SlugField(default='ccc', max_length=200),
            preserve_default=False,
        ),
    ]
