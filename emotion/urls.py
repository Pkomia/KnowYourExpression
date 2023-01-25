# from django.contrib import admin
from django.urls import path , include

from . import views
 

urlpatterns = [
    path('', views.index, name='index'),
    path('feature/', views.feature, name='feature'),
    path('about/', views.about, name='about'),
    path('check/', views.check, name='check'),
]