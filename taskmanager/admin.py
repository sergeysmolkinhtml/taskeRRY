from django.contrib import admin
from .models import Desk,Column,Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


admin.site.register(Desk)
admin.site.register(Column)
admin.site.register(Card,CardAdmin)



