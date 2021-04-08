from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.TaskList.as_view(), name = 'list'),
    path('create/', views.CreateTask.as_view(), name = 'create'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.DeleteTask.as_view(), name = 'delete'),
    path('create_task/', views.create_task, name='create_task'),
]