"""taskerDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from taskmanager import views
from taskmanager.api import *
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=True)
router.register('api/v1/users', UserViewSet, basename='user')
router.register('api/v1/cards',CardViewSet, basename='card')
router.register('api/v1/columns',ColumnViewSet,basename='column')

print(router.urls,sep='-')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index.as_view(),name='main'),
    path('app/',include('taskmanager.urls',namespace='taskmanager')),
    path('accounts/',include('allauth.urls')),

    #generic apis
    path('api/v1/desk-list-create/',DeskListCreateAPIView.as_view()),
    path('api/v1/desk-edit/<int:pk>/',DeskRetrieveUpdateDestroyAPIView.as_view()),

]

urlpatterns += router.urls
