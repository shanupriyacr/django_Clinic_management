"""
URL configuration for clinic_management project.

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

from hospitalapp import views

app_name = 'hospitalapp'


urlpatterns = [
    # Home page URL
    path('', views.home_view, name='home'),

    # User login URL
    path('login/', views.user_login, name='login'),

    # User registration URL
    path('register/', views.user_register, name='register'),

    # Book appointment URL
    path('book_appointment/', views.book_appointment, name='book_appointment'),

    # Manage time slots URL
    path('manage_time_slots/', views.manage_time_slots, name='manage_time_slots'),

    # Add doctor URL


    # Edit doctor URL


    # Department list URL
    path('department_list/', views.department_list, name='department_list'),

    # Create department URL
    path('create_department/', views.create_department, name='create_department'),

    # Edit department URL
    path('edit_department/<int:department_id>/', views.edit_department, name='edit_department'),

    # Delete department URL
    path('delete_department/<int:department_id>/', views.delete_department, name='delete_department'),

]







