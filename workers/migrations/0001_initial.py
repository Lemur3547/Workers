# Generated by Django 4.2 on 2024-12-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('team', models.IntegerField(verbose_name='Номер бригады')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('specialization', models.CharField(max_length=100, verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]