from django.db import models


# Create your models here.
class Celebrities(models.Model):
    title = models.CharField('Имя знаменитости', max_length=50)
    description = models.TextField('Биография')
    link = models.TextField("Ссылка на фото", default='Ссылка на фото')
    type = models.CharField('Тип знаменитости', max_length=50, default='тип знаменитости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Знаменитости'
        verbose_name_plural = 'Все'


class Maths(models.Model):
    title = models.CharField('Имя знаменитости', max_length=50)
    description = models.TextField('Биография')
    link = models.TextField("Ссылка на фото", default='Ссылка на фото')
    type = models.CharField('Тип знаменитости', max_length=50, default='тип знаменитости')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Знаменитости по математике'
        verbose_name_plural = 'Математика'


class Literature(models.Model):
    title = models.CharField('Имя знаменитости', max_length=50)
    description = models.TextField('Биография')
    link = models.TextField("Ссылка на фото", default='Ссылка на фото')
    type = models.CharField('Тип знаменитости', max_length=50, default='тип знаменитости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Знаменитости по литературе'
        verbose_name_plural = 'Литература'


class Film(models.Model):
    title = models.CharField('Имя знаменитости', max_length=50)
    description = models.TextField('Биография')
    link = models.TextField("Ссылка на фото", default='Ссылка на фото')
    type = models.CharField('Тип знаменитости', max_length=50, default='тип знаменитости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Знаменитости на киноиндустрий'
        verbose_name_plural = 'Киноиндустрия'