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
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = routers.DefaultRouter(trailing_slash=True)
router.register('api/v1/users', UserViewSet, basename='user')
router.register('api/v1/cards',CardViewSet, basename='card')
router.register('api/v1/columns',ColumnViewSet,basename='column')

print(router.urls,sep='-')


urlpatterns = [
    path('grappelli/',include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('',views.index.as_view(),name='main'),
    path('app/',include('taskmanager.urls',namespace='taskmanager')),
    path('accounts/',include('allauth.urls')),
    path('api/v1/auth/',include('djoser.urls')),
    path('api/v1/auth/',include('djoser.urls.authtoken')),
    path('api/v1/auth/',include('djoser.urls.jwt')),

    path('api/v1/token/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('api/v1/token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('api/v1/token/verify/',TokenVerifyView.as_view(),name = 'token_verify'),

    #generic apis
    path('api/v1/desk-list-create/',DeskListCreateAPIView.as_view()),
    path('api/v1/desk-edit/<int:pk>/',DeskRetrieveUpdateDestroyAPIView.as_view()),

]

urlpatterns += router.urls
