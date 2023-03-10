# Generated by Django 3.2.9 on 2023-02-17 07:15

import company.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20230213_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='loga',
            field=models.ImageField(blank=True, null=True, upload_to=company.services.get_upload_path, validators=[company.services.validate_file_extension], verbose_name='Логотип нашего партнёра *(157x127)'),
        ),
    ]
