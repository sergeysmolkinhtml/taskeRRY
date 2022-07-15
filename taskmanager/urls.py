from django.contrib import admin
from django.urls import path,include,register_converter,re_path
from . import views
from .views import *

app_name = 'taskmanager'

urlpatterns = [
    path('desks/',views.DesksList.as_view(),name = 'desk-list'),
    path('desks/<int:pk>/',views.DeskDetail.as_view(),name = 'desk-detail'),
    path('create-desk',views.CreateDesk.as_view(),name = 'create-desk'),
    path('create-column/',views.CreateColumn.as_view(),name = 'create-column'),
    path('create-card/',views.CreateCard.as_view(),name = 'create-card'),
    path('card/<int:pk>/',views.CardDetail.as_view(),name = 'card-detail'),
    path('card-update/<int:pk>/',views.CardUpdate.as_view(),name = 'card-update'),
    path('card-delete/<int:pk>/',views.CardDelete.as_view(),name = 'card-delete')
]