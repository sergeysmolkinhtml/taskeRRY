# Generated by Django 4.0.4 on 2022-07-14 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name_plural': 'Карточки'},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'verbose_name_plural': 'Колонки'},
        ),
        migrations.AlterModelOptions(
            name='desk',
            options={'verbose_name': 'Доска', 'verbose_name_plural': 'Доски'},
        ),
    ]
