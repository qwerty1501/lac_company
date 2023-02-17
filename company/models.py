from django.db import models

from .services import get_upload_path, validate_file_extension


class CreateStaff(models.Model):
    class Meta:
        db_table = 'company'
        verbose_name = 'Специалиста'
        verbose_name_plural = 'Специалисты'
    
    image = models.ImageField(verbose_name='Фотография', upload_to ='image/person')
    name = models.CharField(verbose_name='Ваша полная имя', max_length=20, blank=True, null=True)
    position = models.CharField(verbose_name='Должность', max_length=50, blank=True, null=True)
   
    def __str__(self):
        return self.name
    
    
class Services(models.Model):
    class Meta:
        db_table = 'services'
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        
    name = models.CharField(verbose_name='Полное название', max_length=256)
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.name
    
    
class Partners(models.Model):
    class Meta:
        db_table = 'partners'
        verbose_name = 'партнеров'
        verbose_name_plural = 'Наши партнёры'
        
    loga = models.ImageField(verbose_name="Логотип нашего партнёра *(157x127)", upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    description = models.TextField(verbose_name='Опишите нашего партнёра')
    
    
class Reviews(models.Model):
    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
    
    name = models.CharField(verbose_name='Полное имя', max_length=64)
    description = models.TextField(verbose_name='Отзывы')
    
    def __str__(self):
        return self.name