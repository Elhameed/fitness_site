"""
URL configuration for fitness_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from fitflexx import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', views.classes, name='classes'),
    path('register/', views.register, name='register'),
    path('book_class/<int:class_id>/', views.book_class, name='book_class'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.user_profile, name='profile'),
]

