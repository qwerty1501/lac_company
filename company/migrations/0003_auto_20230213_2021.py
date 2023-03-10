# Generated by Django 3.2.9 on 2023-02-13 14:21

import company.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20230213_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'партнеров', 'verbose_name_plural': 'Наши партнёры'},
        ),
        migrations.AlterField(
            model_name='partners',
            name='loga',
            field=models.ImageField(blank=True, null=True, upload_to=company.services.get_upload_path, validators=[company.services.validate_file_extension], verbose_name='Логотип нашего партнёра'),
        ),
    ]
