# Generated by Django 3.2.9 on 2023-02-07 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
    ]