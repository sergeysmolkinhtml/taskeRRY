# Generated by Django 4.0.4 on 2022-07-13 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=233, verbose_name='Название колонки')),
                ('position', models.IntegerField(verbose_name='Позиция колонки')),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=233, verbose_name='Название доски')),
                ('type', models.IntegerField(choices=[(1, 'Table'), (2, 'Board')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=233, verbose_name='Название карточки')),
                ('description', models.TextField(max_length=777, verbose_name='Описание')),
                ('position', models.IntegerField(verbose_name='Позиция карточки')),
                ('draft', models.BooleanField(default=True, verbose_name='Черновик')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Отредактировано')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='taskmanager.column', verbose_name='Колонка')),
                ('user_accepted_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто взял таск')),
            ],
        ),
    ]