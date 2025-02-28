from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home , name='home'),
    path('register/', views.register , name='register'),
    path('user_login/', views.user_login , name='login'),
    path('user_logout/', views.user_logout , name='logout'),
    path('todo', views.todo , name='todo'), 
    path('todo/delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Fix URL pattern
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
]

