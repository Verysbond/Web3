from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50, default="default title")
    task = models.TextField('Описание', max_length=250, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    # def __str__(self):
    #     return f'{self.title}'
    #     # return self.title