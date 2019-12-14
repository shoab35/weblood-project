from django.contrib import admin
from django.urls import path, include
from . import views
# TEMPLATE URLS
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
