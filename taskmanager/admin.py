from django.contrib import admin
from .models import Desk,Column,Card,Profile
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','column',)

admin.site.register(Profile)
admin.site.register(Desk)
admin.site.register(Column)
admin.site.register(Card,CardAdmin)



