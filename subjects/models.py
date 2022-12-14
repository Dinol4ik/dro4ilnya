from django.db import models


# Create your models here.
class subjects(models.Model):
    title = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.title


class Curse(models.Model):
    subject = models.ForeignKey(subjects,on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    about = models.TextField('О курсе')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title
