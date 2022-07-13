from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

DeskType = [
    (1,'Table'),
    (2,'Board'),
]
class Desk(models.Model):
    title = models.CharField(max_length=233,verbose_name='Название доски')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    type = models.IntegerField(choices=DeskType)


class Column(models.Model):
    title = models.CharField(max_length=233,verbose_name='Название колонки')
    position = models.IntegerField(verbose_name='Позиция колонки')


class Card(models.Model):
    title = models.CharField(max_length=233,verbose_name='Название карточки')
    description = models.TextField(max_length=777,verbose_name='Описание')
    position = models.IntegerField(verbose_name='Позиция карточки')
    draft = models.BooleanField(default=True,verbose_name='Черновик')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Когда создано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Отредактировано')
    column = models.ForeignKey('Column',on_delete=models.DO_NOTHING,verbose_name='Колонка')
    user_accepted_task = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Кто взял таск')