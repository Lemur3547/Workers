from django.db import models

# Create your models here.


class Worker(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    team = models.IntegerField(verbose_name='Номер бригады')
    salary = models.IntegerField(verbose_name='Зарплата')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
