from django.contrib import admin
from django.urls import path, include
from . import views
# TEMPLATE URLS
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search/', views.search, name='search'),
]
