# Generated by Django 3.2.9 on 2023-02-07 11:45

from django.db import migrations, models
import news.services


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=news.services.get_upload_path, verbose_name='Фотография'),
        ),
    ]
