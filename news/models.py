from django.db import models

from .services import get_upload_path, validate_file_extension


class News(models.Model):
    class Meta:
        db_table = 'news'
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
    
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    images = models.ImageField(verbose_name="Фотография", upload_to=get_upload_path, null=True, blank=True)
    description = models.TextField(verbose_name="Описание")
    data = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)
    
    def __str__(self):
        return self.title
    