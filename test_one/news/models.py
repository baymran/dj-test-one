from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150,verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return f'OBJECT: <{self.title}, id:{self.pk}>'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('read_more', kwargs={'news_id': self.pk})

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})





