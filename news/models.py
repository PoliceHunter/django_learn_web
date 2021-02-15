from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('News')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"