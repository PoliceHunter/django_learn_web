from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('admin/', views.contacts, name='admin'),
]